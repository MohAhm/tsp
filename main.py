from genetic_algorithm import GeneticAlgorithm
from city import City
from route import Route

POPULATION_SIZE = 50
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.8

data = [
    (565.0, 575.0), (25.0, 185.0),
    (345.0, 750.0), (945.0, 685.0),
    (845.0, 655.0), (880.0, 660.0)
]


def main():
    """ EntryPoint """

    # 1 Create list of cities
    cities = []
    for i, axis in enumerate(data, 1):
        cities.append(City(i, axis[0], axis[1]))

    # 2 Create GA object
    ga = GeneticAlgorithm(POPULATION_SIZE, MUTATION_RATE, CROSSOVER_RATE, 0)

    # 3 Initialize population
    initial_population = ga.init_population(len(data))

    # 4 Evaluate population
    ga.eval_population(initial_population, cities)

    fittest = initial_population.get_fittest()
    route = Route(fittest, cities)
    print('Route: ', route, ' Fitness: ', fittest.get_fitness())

    # for chromosome in initial_population.get_population():
    # route = Route(chromosome, cities)
    # print('Route: ', route, ' Total Distance: ', route.total_distance())
    # print('Route: ', route, ' Fitness: ', chromosome.get_fitness())


if __name__ == '__main__':
    main()
