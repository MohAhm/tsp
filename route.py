from individual import Individual


class Route:
    def __init__(self, individual, cities):
        chromosome = individual.chromosome
        self.route = []

        # Build an array of city objects in the order of the
        # individual’s chromosome
        for i in range(len(chromosome)):
            self.route.append(cities[chromosome[i]])

        # Add ending point which is the starting city to the route
        self.route.append(self.route[0])

    def __repr__(self):
        return '->'.join(str(r) for r in self.route)
