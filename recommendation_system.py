ratings = {
    'Rishitha': {'Maharshi': 5, 'Athadu': 3, 'Spyder': 4},
    'Sruthi': {'Crushed': 4, 'Half CA': 5, 'Maharshi': 3},
    'Manaswini': {'Rangasthalam': 2, 'Orange': 5, 'Bheeshma': 5},
}

def cosine_similarity(user1_ratings, user2_ratings):
    common_items = set(user1_ratings.keys()) & set(user2_ratings.keys())
    if not common_items:
        return 0
    dot_product = sum(user1_ratings[item] * user2_ratings[item] for item in common_items)
    magnitude1 = sum(user1_ratings[item]**2 for item in common_items) ** 0.5
    magnitude2 = sum(user2_ratings[item]**2 for item in common_items) ** 0.5
    return dot_product / (magnitude1 * magnitude2)

def recommend(user, ratings, n_recommendations=2):
    scores = {}
    for other_user, other_ratings in ratings.items():
        if other_user == user:
            continue
        similarity = cosine_similarity(ratings[user], other_ratings)
        for item, rating in other_ratings.items():
            if item not in ratings[user]:
                scores[item] = scores.get(item, 0) + similarity * rating
    recommended_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [item for item, score in recommended_items[:n_recommendations]]

# Example: Recommend for Rishitha
print("Recommended for Rishitha:", recommend('Rishitha', ratings))
