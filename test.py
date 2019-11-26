import numpy as np
from math import pow, sqrt
from city import City
from route import Route
# from collections import namedtuple

arr = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52
])


data = [
    (565.0, 575.0), (25.0, 185.0),
    (345.0, 750.0), (945.0, 685.0),
    (845.0, 655.0), (880.0, 660.0)
]

# arr2 = np.empty(len(data), dtype=tuple)
# arr2 = data

# print(arr2)
# np.random.shuffle(arr2)
# print(arr2)
# print(type(arr2[0]))

# initial_population = np.empty((0, len(arr)), dtype=np.uint8)
initial_population = np.empty((0, len(data)))

# for _ in range(len(arr2)):
#     np.random.shuffle(arr2[1:])
#     initial_population = np.append(
#         initial_population, [arr2], axis=0)

# for _ in range(len(data)):
#     route = Route(data)
#     np.random.shuffle(route.chromosome[1:])
#     initial_population = np.append(
#         initial_population, [route.chromosome], axis=0)

# for x in range(len(data)):
# np.random.shuffle(arr[1:])
# route = Route(data)
# print(route.chromosome)
# route = np.random.permutation(route.chromosome)
# initial_population.append(Route(data))
# initial_population = np.append(
#     initial_population, [route], axis=0)

arr = []
for i, axis in enumerate(data, 1):
    arr.append(i)

copy = arr[1:]
np.random.shuffle(arr[1:])
arr[1:] = copy
print(arr)


print(initial_population)
# print(initial_population[4][4].x, initial_population[4][4].id)
# print(type(initial_population[4]))
# print(matrix[3][2])
# print(len(matrix))


# test = pow(3, 2)
# print(test)
# test = sqrt(test)
# print(test)


# c1 = City(565.0, 575.0)
# c2 = City(25.0, 185.0)

# result = c1.distance_from(c2)
# print(result)


# Coordinate = namedtuple('Coordinate', 'x, y')

data = [(565.0, 575.0), (25.0, 185.0),
        (345.0, 750.0), (945.0, 685.0), (845.0, 655.0)]


# cities = []
# id = 1
# for x, y in data:
#     cities.append(City(id, x, y))
#     id += 1

cities = []
for i, axis in enumerate(data, 1):
    cities.append(City(i, axis[0], axis[1]))

chromosome = cities

# for gene in chromosome:
#     print(gene.id, gene.x, gene.y)


# letters = ["a", "b", "c", "d"]
# for index, letter in enumerate(letters):
#     print(index, letter)
