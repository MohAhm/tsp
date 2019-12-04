from chromosome import Chromosome


class Population:
    def __init__(self, population_size=0, chromosome_length=0):
        self.population = []

        if population_size and chromosome_length:
            # Create array of chromosomes
            for _ in range(population_size):
                chromosome = Chromosome(chromosome_length)
                self.population.append(chromosome)

    def get_population(self):
        return self.population

    def set_chromosome(self, chromosome):
        self.population.append(chromosome)

    def evaluation(self, chromosome):
        return chromosome.get_fitness()

    def get_fittest(self):
        return min(self.population, key=self.evaluation)
