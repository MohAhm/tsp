from population import Population
from chromosome import Chromosome
from route import Route
import random


class GeneticAlgorithm:
    def __init__(self, population_size, tournament_size, crossover_rate, mutation_rate):
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def init_population(self, chromosome_length):
        population = Population(self.population_size, chromosome_length)
        return population

    def calc_fitness(self, population, cities):
        # Calculate and store each chromosome in the population
        for chromosome in population.get_population():
            route = Route(chromosome, cities)
            chromosome.set_fitness(route.total_distance())

    def eval_fitness(self, population):
        population.elitism_sort()
        return population

    def tournament_selection(self, population):
        # Randomly selected a set of chromosomes from the population
        # then return the chromosome with the highest fitness
        tournament = Population(self.tournament_size)

        i = 0
        while i < self.tournament_size:
            chromosome = random.choice(population.get_population())

            if chromosome not in tournament.get_population():
                # Prevent duplicate chromosomes
                tournament.set_chromosome(i, chromosome)
                i += 1

        return tournament.get_fittest()

    def order_crossover(self, parent1, parent2):
        offspring = Chromosome(parent1.get_length(), False)

        # Crossover probability
        if self.crossover_rate > random.random():
            # Create an offspring from the two selected chromosomes

            # Select two random subset points from first parent
            pot1 = random.randrange(offspring.get_length())
            pot2 = random.randrange(offspring.get_length())

            # print('Parent1: ', parent1.get_chromosome())
            # print('Parent2: ', parent2.get_chromosome())
            # print('Offspring init: ', offspring.get_chromosome())

            # The two positions shouldn't be same
            while (pot1 == pot2):
                pot1 = random.randrange(offspring.get_length())
                pot2 = random.randrange(offspring.get_length())

            # Make the smaller one start point and
            # the larger one end point
            start = min(pot1, pot2)
            end = max(pot1, pot2)

            # print("Start: ", start)
            # print("End: ", end)

            # Copy the subset between the points from the first parent
            # to the offspring
            for i in range(start, end + 1):
                offspring.set_gene(i, parent1.get_gene(i))

            # print('Offspring+(p1): ', offspring.get_chromosome())

            # Copy the remaining unused subset from the second parent
            # to the offspring
            i = 0
            for gene in parent2.get_chromosome():
                while gene not in offspring.get_chromosome():
                    # find empty index
                    if offspring.get_gene(i) == -1:
                        offspring.set_gene(i, gene)

                    i += 1

            # print('Offspring+(p2): ', offspring.get_chromosome())
        else:
            # Otherwise create a new offspring identical
            # to the parent
            for i in range(parent1.get_length()):
                offspring.set_gene(i, parent1.get_gene(i))

        return offspring

        # return parent1

    def swap_mutation(self, offspring):

        # for i in range(1, offspring.get_length()):
        #     if self.mutation_rate > random.random():
        #         # print('Offspring (init): ', offspring.get_chromosome())

        #         pos = random.randrange(offspring.get_length())

        #         while (i == pos) or (pos == 0):
        #             pos = random.randrange(offspring.get_length())

        #         # Get genes to swap
        #         gene1 = offspring.get_gene(i)
        #         gene2 = offspring.get_gene(pos)

        #         # Swap genes
        #         offspring.set_gene(pos, gene1)
        #         offspring.set_gene(i, gene2)

        #         # print('Offspring (muta): ', offspring.get_chromosome())

        # return offspring

        # Mutation probability
        if self.mutation_rate > random.random():
            # print('Offspring (init): ', offspring.get_chromosome())

            # Select two random positions
            pos1 = random.randrange(offspring.get_length())
            pos2 = random.randrange(offspring.get_length())

            # The positions shouldn't be same,
            # and shouldn't be same first index
            while (pos1 == pos2) or (pos1 == 0) or (pos2 == 0):
                pos1 = random.randrange(offspring.get_length())
                pos2 = random.randrange(offspring.get_length())

            # print(pos1)
            # print(pos2)

            # Get genes to swap
            gene1 = offspring.get_gene(pos1)
            gene2 = offspring.get_gene(pos2)

            # Swap genes
            offspring.set_gene(pos2, gene1)
            offspring.set_gene(pos1, gene2)

            # print('Offspring (muta): ', offspring.get_chromosome())

        return offspring
