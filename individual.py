import numpy as np


class Individual:  # (Chromosome)
    def __init__(self, chromosome_length):
        # Create a chromosome with each city’s (gene) index
        individual = []
        for i in range(chromosome_length):
            individual.append(i)

        # Randomize the initial chromosome except the starting city/point
        self.chromosome = np.array(individual)
        np.random.shuffle(self.chromosome[1:])

        self.fitness = 0

    def unique(self):
        # Checks if all the elements in a list are unique
        if len(self.chromosome) == len(set(self.chromosome)):
            return True
        else:
            return False
