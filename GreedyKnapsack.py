'''
    A greedy approach to the common knapsack problem
'''


def knapsack(vals, weights, max_weight):
    ratios = []
    ans = []
    curr_weight = 0
    for i in range(len(vals)):
        ratios.append((i, float(vals[i]) / float(weights[i])))
    ratios.sort(key=lambda x: x[1], reverse=True)
    for j in range(len(ratios)):
        if curr_weight + weights[ratios[j][0]] <= max_weight:
            curr_weight += weights[ratios[j][0]]
            ans.append(vals[ratios[j][0]])
    return ans


vals = [1, 2, 3, 4]
weights = [2, 6, 7, 1]
max_weight = 13
print(knapsack(vals, weights, max_weight))
