from city import City
from individual import Individual
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


individual = Individual(len(data))
print('Individual chromosome: ', individual.chromosome)


route = Route(individual, cities)
print('Route Test: ', route.route)

for i, city in enumerate(route.route):
    # print(i)
    print(city.x, city.y)

print('Total Distance: ', route.get_distance())


initial_population = Population(10, len(data))
# print('Population: ', initial_population.population)

for individual in initial_population.population:
    # print(individual.chromosome)
    route = Route(individual, cities)
    print('Route: ', route)


# test = ['(1)', '(2)', '(6)', '(3)', '(5)', '(4)', '(1)']
# print('->'.join(test))
