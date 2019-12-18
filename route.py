from chromosome import Chromosome
from city import City


class Route:
    def __init__(self, chromosome, cities):
        self.route = []
        self.distance = 0

        # Build an array of city objects in the order
        # of the chromosome
        for i in range(chromosome.get_length()):
            gene = chromosome.get_gene(i)
            self.route.append(cities[gene])

        # Add ending point which is the starting city to the route
        self.route.append(self.route[0])

    def total_distance(self):
        # Loop over cities in route and calculate route distance
        for i, city in enumerate(self.route[:-1]):
            self.distance += city.distance_from(self.route[i + 1])

        return self.distance

    def __repr__(self):
        return '->'.join(str(r) for r in self.route)
