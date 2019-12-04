# import numpy as np
import random

# lst = [4, 3, 5, 1, 2]

# print(min(lst))

# for i, num in enumerate(lst[:-1]):
#     test = min(num, lst[i + 1])

# print(test)

# test = lst[0]

# for i in lst:
#     if i < test:
#         test = i

# print(test)


# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = np.random.choice(lst)
# print(a)


# tournament = []
# tournament_size = 5
# i = 0

# while i < tournament_size:
#     a = random.choice(lst)

#     if a not in tournament:
#         tournament.append(a)
#         i += 1

# print(tournament)


# num = 0

# if num:
#     print('Good')


# population = np.empty(5, dtype=object)
# print(population)

# population = np.append(population, 1)
# print(population)


lst = list(range(60))
# random.shuffle(lst[1:])

tmp = lst[1:]
random.shuffle(tmp)
lst[1:] = tmp

print(lst)
