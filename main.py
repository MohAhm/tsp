from genetic_algorithm import GeneticAlgorithm
from city import City
from route import Route

POPULATION_SIZE = 50
TOURNAMENT_SIZE = 5
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

ELITISM = 24

# TERMINATION = 3000


def read_file(filename):
    file_object = open(filename)
    data = []

    while True:
        line = file_object.readline()

        if not line:
            break

        elif line[0].isdigit():
            xy = tuple(line.strip().split())
            data.append((float(xy[1]), float(xy[2])))

    file_object.close()
    return data


def main():
    """ EntryPoint """

    # Read data from a file
    data = read_file('Assignment 3 berlin52.tsp')

    # Create list of cities
    cities = []
    for i, axis in enumerate(data, 1):
        cities.append(City(i, axis[0], axis[1]))

    # Create GA object
    ga = GeneticAlgorithm(POPULATION_SIZE, TOURNAMENT_SIZE,
                          CROSSOVER_RATE, MUTATION_RATE)

    # Initialize population
    population = ga.init_population(len(data))
    # Set the fitness for each chromosome
    ga.calc_fitness(population, cities)

    # similarity = 0
    generation = 0
    while True:
        # previous_fittest = population.get_fittest()

        # Evaluate the fitness F(x) of the population
        population = ga.eval_fitness(population)
        current_fittest = population.get_fittest()

        # if current_fittest.get_fitness() == previous_fittest.get_fitness():
        #     # If there has been no improvement in the fittest solution,
        #     # increment the counter
        #     similarity += 1
        # else:
        #     # Otherwise, if there are improvement reset the counter
        #     similarity = 0

        # # Termination condition:
        # # If the fitness value does not improve for a considerable
        # # amount of time
        # if similarity == TERMINATION:
        #     break

        if 9000 > current_fittest.get_fitness():
            break

        print('Generation: ', generation)
        print('Best distance: ', current_fittest.get_fitness())

        # print(generation, ' ', current_fittest.get_fitness())

        # Skipp elite chromosomes
        it = iter(range(ELITISM, POPULATION_SIZE))
        # Loop over current population
        for i in it:
            # Select two chromosomes
            parent1 = ga.tournament_selection(population)
            parent2 = ga.tournament_selection(population)

            # Apply crossover
            offspring1 = ga.order_crossover(parent1, parent2)
            offspring2 = ga.order_crossover(parent2, parent1)

            # Mutate the two chromosomes
            offspring1 = ga.swap_mutation(offspring1)
            offspring2 = ga.swap_mutation(offspring2)

            # Set fitness
            route1 = Route(offspring1, cities)
            offspring1.set_fitness(route1.total_distance())
            route2 = Route(offspring2, cities)
            offspring2.set_fitness(route2.total_distance())

            # Place the resulting chromosomes into the population
            population.set_chromosome(i, offspring1)
            population.set_chromosome(next(it), offspring2)

        generation += 1

    fittest = population.get_fittest()
    route = Route(fittest, cities)
    print('The Best distance: ', route.total_distance())
    print('Shortest route: ', route)
    # print('Chromosome: ', fittest.get_chromosome())


if __name__ == '__main__':
    main()
