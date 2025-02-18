def k_most_frequent(lst, k):
    if len(lst) == 0:
        return []
    counts = {}

    for e in lst:
        counts[e] = counts.get(e, 0) + 1
    leaderboard = sorted(counts, key=lambda x: counts[x], reverse=True)

    i = min(len(leaderboard) - 1, k)
    ith_count = counts[leaderboard[i - 1]]

    while i < len(leaderboard) and counts[leaderboard[i]] == ith_count:
        i += 1
    return leaderboard[:i]

print(k_most_frequent([1, 1, 1, 2, 2, 3], 2))
    
    
