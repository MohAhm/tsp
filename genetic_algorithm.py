from population import Population


class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count):
        self.population = population_size
        self.mutation = mutation_rate
        self.crossover = crossover_rate
        self.elitism = elitism_count

    def init_population(self, chromosome):
        population = Population(self.population, chromosome)
        return population
