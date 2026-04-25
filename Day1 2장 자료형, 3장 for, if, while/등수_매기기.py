def solution(score):
    avr = []
    for i, j in score:
        avr.append(i+j)
    ranks = []
    for p in avr:
        rank = 1
        for q in avr:
            if p < q:
                rank += 1
        ranks.append(rank)
        
    return ranks
