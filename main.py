from genetic_algorithm import GeneticAlgorithm
from city import City
from route import Route

POPULATION_SIZE = 100
TOURNAMENT_SIZE = 5
CROSSOVER_RATE = 0.8    # 80%
MUTATION_RATE = 0.1    # 10%

ELITISM = 2     # must be even number

GENERATIONS_MAX = 3000  # tmp

data = [
    (565.0, 575.0), (25.0, 185.0),
    (345.0, 750.0), (945.0, 685.0),
    (845.0, 655.0), (880.0, 660.0),
    (25.0, 230.0), (525.0, 1000.0),
    (580.0, 1175.0), (650.0, 1130.0)
]


def main():
    """ EntryPoint """

    # 1 Create list of cities
    cities = []
    for i, axis in enumerate(data, 1):
        cities.append(City(i, axis[0], axis[1]))

    # 2 Create GA object
    ga = GeneticAlgorithm(POPULATION_SIZE, TOURNAMENT_SIZE,
                          CROSSOVER_RATE, MUTATION_RATE)

    # 3 Initialize population
    population = ga.init_population(len(data))
    # Set the fitness F(x) for each chromosome
    ga.calc_fitness(population, cities)

    generation = 1
    while GENERATIONS_MAX > generation:
        # print('Generation: ', generation)

        # Evaluate the fitness F(x) of the population
        population = ga.eval_fitness(population)

        # for chromosome in population.get_population():
        #     route = Route(chromosome, cities)
        #     print('Distance: ', route.total_distance())

        fittest = population.get_fittest()
        route = Route(fittest, cities)
        print('Best distance: ', route.total_distance())

        # Skipp elite chromosomes, which are the two first indices
        it = iter(range(ELITISM, POPULATION_SIZE))
        # Loop over current population
        for i in it:
            # Select two chromosomes
            parent1 = ga.tournament_selection(population)
            parent2 = ga.tournament_selection(population)

        #   Apply crossover
            offspring1 = ga.order_crossover(parent1, parent2)
            offspring2 = ga.order_crossover(parent2, parent1)

        #   Mutate the two chromosomes
            offspring1 = ga.swap_mutation(offspring1)
            offspring2 = ga.swap_mutation(offspring2)

        #   Set fitness
            route1 = Route(offspring1, cities)
            offspring1.set_fitness(route1.total_distance())
            route2 = Route(offspring2, cities)
            offspring2.set_fitness(route2.total_distance())

        #   Place the resulting chromosomes into the population
            # print(i, next(it))
            population.set_chromosome(i, offspring1)
            population.set_chromosome(next(it), offspring2)

        generation += 1

    fittest = population.get_fittest()
    route = Route(fittest, cities)
    print('The Best distance: ', route.total_distance())
    print('Route: ', route)


if __name__ == '__main__':
    main()
