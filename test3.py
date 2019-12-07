import random

# t1 = random.random()
# print(t1)

mutationRate = 0.1
r = random.random()
if mutationRate > r:
    print('ok')
print(r)


lst = ['A', 'B', 'C', 'D', 'E', 'G', 'H', 'L']

# for i, c in enumerate(lst):
#     print(i)

# t1 = 0
# for i in range(5, 50):
#     print(t1)
#     t1 = t1 + i

# it = iter(lst[2:])
it = iter(range(2, 50))
for x in it:
    print(x, next(it))
