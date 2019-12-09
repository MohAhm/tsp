from chromosome import Chromosome


class Population:
    def __init__(self, population_size, chromosome_length=0):
        self.population = [None] * population_size

        if chromosome_length:
            # Create array of chromosomes
            for i in range(population_size):
                chromosome = Chromosome(chromosome_length)
                self.population[i] = chromosome

    def get_population(self):
        return self.population

    def set_chromosome(self, index, chromosome):
        self.population[index] = chromosome

    def evaluation(self, chromosome):
        return chromosome.get_fitness()

    def elitism_sort(self):
        self.population = sorted(self.population, key=self.evaluation)

    def get_fittest(self):
        return self.population[0]
