from population import Population
from route import Route


class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count

    def init_population(self, chromosome_length):
        population = Population(self.population_size, chromosome_length)
        return population

    def eval_population(self, population, cities):
        for chromosome in population.get_population():
            route = Route(chromosome, cities)
            chromosome.set_fitness(route.total_distance())
