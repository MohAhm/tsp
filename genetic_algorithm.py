

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count):
        self.population = population_size
        self.mutation = mutation_rate
        self.crossover = crossover_rate
        self.elitism = elitism_count

    # def init_population(self):
    # def calc_fitness(self):
    # def eval_population(self):
    # def is_termination_condition_met(self):
    # def select_parent(self):
    # def crossover_population(self):
    # def mutate_population(self):


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
