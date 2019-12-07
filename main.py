from genetic_algorithm import GeneticAlgorithm
from city import City
from route import Route

POPULATION_SIZE = 50
TOURNAMENT_SIZE = 5
CROSSOVER_RATE = 0.8    # 80%
MUTATION_RATE = 0.15    # 15%

ELITISM = 2     # must be even number

GENERATIONS_MAX = 5  # tmp

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

    chromosome_length = len(data)

    # 2 Create GA object
    ga = GeneticAlgorithm(POPULATION_SIZE, TOURNAMENT_SIZE,
                          CROSSOVER_RATE, MUTATION_RATE)

    # 3 Initialize population
    population = ga.init_population(chromosome_length)
    # Set the fitness F(x) for each chromosome
    ga.calc_fitness(population, cities)

    generation = 1
    while GENERATIONS_MAX > generation:
        print('Generation: ', generation)

        # Evaluate the fitness F(x) of the population
        ga.eval_fitness(population)

        fittest = population.get_fittest()
        route = Route(fittest, cities)
        print('Route: ', route, ' Fitness: ', fittest.get_fitness())

        # Ignore elite chromosomes, which are the two first indices
        it = iter(range(ELITISM, POPULATION_SIZE))
        # Loop over current population
        for i in it:
            # Select two chromosomes
            parent1 = ga.tournament_selection(population)
            parent2 = ga.tournament_selection(population)

        #   Apply crossover
        #       Create two new offspring from the two selected chromosomes
        #       Otherwise return the parent back
            offspring1 = ga.order_crossover(
                parent1, parent2, chromosome_length)
            offspring2 = ga.order_crossover(
                parent2, parent1, chromosome_length)

        #   Mutate the two chromosomes

        #   Set fitness
            route = Route(offspring1, cities)
            offspring1.set_fitness(route.total_distance())
            route = Route(offspring2, cities)
            offspring2.set_fitness(route.total_distance())

            # print('Offspring1:', offspring1.get_fitness())
            # print('Offspring2:', offspring2.get_fitness())

        #   Place the resulting chromosomes into the population
            population.set_chromosome(i, offspring1)
            population.set_chromosome(next(it), offspring2)

        generation += 1

    # for chromosome in population.get_population():
    #     route = Route(chromosome, cities)
    #     print('Route: ', route, ' Fitness: ', chromosome.get_fitness())


if __name__ == '__main__':
    main()
