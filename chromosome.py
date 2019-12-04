import random


class Chromosome:
    def __init__(self, chromosome_length):
        # Create a chromosome with each city’s (gene) index
        self.chromosome = []
        self.fitness = 0

        for i in range(chromosome_length):
            self.chromosome.append(i)

        # Randomize the initial chromosome except the starting city/point
        tmp = self.chromosome[1:]
        random.shuffle(tmp)
        self.chromosome[1:] = tmp

    def get_chromosome(self):
        return self.chromosome

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness
