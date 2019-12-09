import random

mutationRate = 0.15


offspring = list(range(1, 15))
tmp = offspring[1:]
random.shuffle(tmp)
offspring[1:] = tmp

print('Offspring: ', offspring)


for i in range(1, len(offspring)):
    # Get new gene position
    r = random.random()
    if mutationRate > r:
        pos = random.randrange(len(offspring))
        while (i == pos) or (pos == 0):
            pos = random.randrange(len(offspring))
        # Get genes to swap
        print(i, pos)
        offspring[i], offspring[pos] = offspring[pos], offspring[i]
        print(r)

print('Offspring: ', offspring)


# r = random.random()
# if mutationRate > r:
#     pos1 = random.randrange(len(offspring))
#     pos2 = random.randrange(len(offspring))

#     # Rules: The indexes shouldn't be the same
#     while (pos1 == pos2) or (pos1 == 0) or (pos2 == 0):
#         pos1 = random.randrange(len(offspring))
#         pos2 = random.randrange(len(offspring))

#     print(pos1)
#     print(pos2)

#     offspring[pos2], offspring[pos1] = offspring[pos1], offspring[pos2]

# print('Offspring: ', offspring)
# print(r)
