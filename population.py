import numpy as np
from individual import Individual


class Population:
    def __init__(self, population_size, chromosome_length):
        population = np.empty(0, dtype=object)

        # Create array of individuals
        for _ in range(population_size):
            individual = Individual(chromosome_length)
            population = np.append(
                population, individual)

        self.population = population
