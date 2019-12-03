import numpy as np
from chromosome import Chromosome


class Population:
    def __init__(self, population_size, chromosome_length):
        self.population = np.empty(0, dtype=object)

        # Create array of chromosomes
        for _ in range(population_size):
            chromosome = Chromosome(chromosome_length)
            self.population = np.append(
                self.population, chromosome)

    def get_population(self):
        return self.population

    def evaluation(self, chromosome):
        return chromosome.get_fitness()

    def get_fittest(self):
        return min(self.population, key=self.evaluation)
