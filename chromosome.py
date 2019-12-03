import numpy as np


class Chromosome:
    def __init__(self, chromosome_length):
        # Create a chromosome with each city’s (gene) index
        self.chromosome = []
        self.fitness = 0

        for i in range(chromosome_length):
            self.chromosome.append(i)

        # Randomize the initial chromosome except the starting city/point
        self.chromosome = np.array(self.chromosome)
        np.random.shuffle(self.chromosome[1:])

    def get_chromosome(self):
        return self.chromosome

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def unique(self):
        # Checks if all the elements in a list are unique
        if len(self.chromosome) == len(set(self.chromosome)):
            return True
        else:
            return False
