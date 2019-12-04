from population import Population
from route import Route
import random


class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count, tournament_size):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.tournament_size = tournament_size

    def init_population(self, chromosome_length):
        population = Population(self.population_size, chromosome_length)
        return population

    def calc_fitness(self, population, cities):
        # Calculate and store each chromosome in the population
        for chromosome in population.get_population():
            route = Route(chromosome, cities)
            chromosome.set_fitness(route.total_distance())

    def tournament_selection(self, population):
        # Randomly selected a set of chromosomes from the population
        # then return the chromosome with the highest fitness
        tournament = Population()

        i = 0
        while i < self.tournament_size:
            chromosome = random.choice(population.get_population())

            if chromosome not in tournament.get_population():
                # Prevent duplicate chromosomes
                tournament.set_chromosome(chromosome)
                i += 1

        # for chromosome in tournament.get_population():
        #     print(chromosome.get_fitness())

        return tournament.get_fittest()
