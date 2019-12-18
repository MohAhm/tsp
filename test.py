import random

parent1 = list(range(15))
parent2 = list(range(15))

tmp = parent2[1:]
random.shuffle(tmp)
parent2[1:] = tmp

offspring1 = [-1] * len(parent1)
offspring2 = [-1] * len(parent1)

print('Parent1: ', parent1)
print('Parent2: ', parent2)
print('Offspring init: ', offspring1)
print('Offspring init: ', offspring2)

pos1 = random.randrange(len(parent1))
pos2 = random.randrange(len(parent1))

# Rules: The indexes shouldn't be the same
while (pos1 == pos2):
    pos1 = random.randrange(len(parent1))
    pos2 = random.randrange(len(parent1))

# print(pos1)
# print(pos2)

start = min(pos1, pos2)
end = max(pos1, pos2) + 1
# end = end + 1

print("Start: ", start)
print("End: ", end)

for idx in range(start, end):
    offspring1[idx] = parent1[idx]

for idx in range(start, end):
    offspring2[idx] = parent1[idx]

print('Offspring+(p1): ', offspring1)
print('Offspring+(p1): ', offspring2)

# t1 = [i for i, e in enumerate(offspring1) if e == 0]
# print(t1)

i = 0
for city in parent2:
    while city not in offspring1:
        # find empty index
        if offspring1[i] == -1:
            offspring1[i] = city

        i += 1

# print('Length: ', len(parent2))

# for i in range(len(parent2)):
#     gene = i + end
#     city = parent2[i]

#     print(gene)

#     while city not in offspring1:
#         if gene >= len(parent2):
#             gene -= len(parent2)

#         if offspring1[gene] == -1:
#             offspring1[gene] = city

#         gene += 1

offspring2[0] = 0
for i in range(len(parent2)):
    gene = i + end

    if gene >= len(parent2):
        gene -= len(parent2)

    # print(gene)

    if parent2[gene] not in offspring2:
        for j in range(len(offspring2)):
            if offspring2[j] == -1:
                offspring2[j] = parent2[gene]
                break


print('Offspring+(p2): ', offspring1)
print('Offspring+(p2): ', offspring2)
