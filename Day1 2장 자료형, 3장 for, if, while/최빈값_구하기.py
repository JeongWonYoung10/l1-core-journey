def solution(array):
    counts = {}
    for i in array:
        counts[i] = counts.get(i , 0) + 1
    countMax = max(counts.values())
    winners = [p for p, q in counts.items() if q == countMax]
    return winners[0] if len(winners) < 2 else -1
