import random


class Chromosome:
    def __init__(self, chromosome_length, init_gene=True):
        # Create a chromosome with each city’s (gene) index
        self.chromosome = [-1] * chromosome_length
        self.fitness = 0

        if init_gene:
            for i in range(chromosome_length):
                self.chromosome[i] = i

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

    def set_gene(self, index, gene):
        self.chromosome[index] = gene

    def get_gene(self, index):
        return self.chromosome[index]
