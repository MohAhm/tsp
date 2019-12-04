import time

from genetic_algorithm import GeneticAlgorithm
from city import City
from route import Route

POPULATION_SIZE = 50
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.8
TOURNAMENT_SIZE = 5

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
    ga = GeneticAlgorithm(POPULATION_SIZE, MUTATION_RATE,
                          CROSSOVER_RATE, 0, TOURNAMENT_SIZE)

    # 3 Initialize population
    initial_population = ga.init_population(len(data))

    # start_time = time.time()
    ga.calc_fitness(initial_population, cities)
    # end_time = time.time()
    # time_taken = (end_time - start_time)*(10**6)
    # print("Time taken for calculating fitness:", time_taken)

    # start_time = time.time()
    fittest = initial_population.get_fittest()
    print('Fittest: ', fittest.get_fitness())
    print('Chromosome: ', fittest.get_chromosome())
    # end_time = time.time()
    # time_taken = (end_time - start_time)*(10**6)
    # print("Time taken for getting the fittest:", time_taken)

    # route = Route(fittest, cities)
    # print('Fittest: ', fittest.get_fitness())
    # print('Route: ', route, ' Fittest: ', fittest.get_fitness())

    # for chromosome in initial_population.get_population():
    #     route = Route(chromosome, cities)
    #     print('Route: ', route, ' Fitness: ', chromosome.get_fitness())

    parent = ga.tournament_selection(initial_population)
    print('Fittest: ', parent.get_fitness())
    print('Chromosome: ', parent.get_chromosome())


if __name__ == '__main__':
    main()
