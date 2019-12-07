import random

parent1 = list(range(1, 15))
parent2 = list(range(1, 15))

tmp = parent2[1:]
random.shuffle(tmp)
parent2[1:] = tmp

offspring = [-1] * len(parent1)

print('Parent1: ', parent1)
print('Parent2: ', parent2)
print('Offspring init: ', offspring)

pos1 = random.randrange(len(parent1))
pos2 = random.randrange(len(parent1))

# Rules: The indexes shouldn't be the same
while (pos1 == pos2):
    pos1 = random.randrange(len(parent1))
    pos2 = random.randrange(len(parent1))

# print(pos1)
# print(pos2)

start = min(pos1, pos2)
end = max(pos1, pos2)

print("Start: ", start)
print("End: ", end)


for idx in range(start, end + 1):

    # print('i: ', i)
    # print('num: ', num)
    offspring[idx] = parent1[idx]

print('Offspring+(p1): ', offspring)

# t1 = [i for i, e in enumerate(offspring) if e == 0]
# print(t1)

i = 0
for city in parent2:
    while city not in offspring:
        # find empty index
        if offspring[i] == -1:
            offspring[i] = city

        i += 1

print('Offspring+(p2): ', offspring)
