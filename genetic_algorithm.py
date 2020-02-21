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
        # then return the chromosome with the best fitness

        tournament = Population(self.tournament_size)
        chromosomes = random.sample(
            population.get_population(), self.tournament_size)

        for i in range(self.tournament_size):
            tournament.set_chromosome(i, chromosomes[i])

        tournament = self.eval_fitness(tournament)
        return tournament.get_fittest()

    def order_crossover(self, parent1, parent2):
        offspring = Chromosome(parent1.get_length(), False)
        chromosome_length = offspring.get_length()

        # Crossover probability
        if self.crossover_rate > random.random():
            # Create an offspring from the selected chromosomes

            # Select two random subset positions from first parent
            pos1 = random.randrange(chromosome_length)
            pos2 = random.randrange(chromosome_length)

            # The two positions shouldn't be same
            while (pos1 == pos2):
                pos1 = random.randrange(chromosome_length)
                pos2 = random.randrange(chromosome_length)

            # Make the smaller one start point and
            # the larger one end point
            start = min(pos1, pos2)
            end = max(pos1, pos2) + 1

            # Copy the subset between the points from the first parent
            # to the offspring
            for i in range(start, end):
                offspring.set_gene(i, parent1.get_gene(i))

            if offspring.get_gene(0) != 0:
                offspring.set_gene(0, 0)

            # Copy the remaining unused subset from the second parent
            # to the offspring
            for i in range(parent2.get_length()):
                idx = i + end

                if idx >= parent2.get_length():
                    idx -= parent2.get_length()

                if parent2.get_gene(idx) not in offspring.get_chromosome():
                    for j in range(offspring.get_length()):
                        if offspring.get_gene(j) == -1:
                            gene = parent2.get_gene(idx)
                            offspring.set_gene(j, gene)
                            break
        else:
            # Otherwise create a new offspring identical
            # to the parent
            for i in range(parent1.get_length()):
                offspring.set_gene(i, parent1.get_gene(i))

        return offspring

    def swap_mutation(self, offspring):
        chromosome_length = offspring.get_length()

        # Mutation probability
        if self.mutation_rate > random.random():
            # Select two random positions
            pos1 = random.randrange(chromosome_length)
            pos2 = random.randrange(chromosome_length)

            # The positions shouldn't be same,
            # and shouldn't be first index
            while (pos1 == pos2) or (pos1 == 0) or (pos2 == 0):
                pos1 = random.randrange(chromosome_length)
                pos2 = random.randrange(chromosome_length)

            # Get genes to swap
            gene1 = offspring.get_gene(pos1)
            gene2 = offspring.get_gene(pos2)

            # Swap genes
            offspring.set_gene(pos2, gene1)
            offspring.set_gene(pos1, gene2)

        return offspring
