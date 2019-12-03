from city import City
from chromosome import Chromosome
from population import Population
from route import Route

data = [
    (565.0, 575.0), (25.0, 185.0),
    (345.0, 750.0), (945.0, 685.0),
    (845.0, 655.0), (880.0, 660.0)
]

cities = []
for i, axis in enumerate(data, 1):
    cities.append(City(i, axis[0], axis[1]))

print('List of cities: ', cities)


chromosome = Chromosome(len(data))
print('Chromosome: ', chromosome.get_chromosome())


route = Route(chromosome, cities)
print('Route Test: ', route.route)

for i, city in enumerate(route.route):
    # print(i)
    # print(city, route.route[i + 1])
    print(city.x, city.y)

print('Total Distance: ', route.total_distance())


initial_population = Population(10, len(data))
# print('Population: ', initial_population.population)

for chromosome in initial_population.get_population():
    route = Route(chromosome, cities)
    print('Route: ', route)


# test = ['(1)', '(2)', '(6)', '(3)', '(5)', '(4)', '(1)']
# print('->'.join(test))
