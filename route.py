from individual import Individual
from city import City


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
        self.distance = 0

    def get_distance(self):
        # Loop over cities in route and calculate route distance
        for i, city in enumerate(self.route[:-1]):
            # print(city, self.route[i + 1])
            self.distance += city.distance_from(self.route[i + 1])

        return self.distance

    def __repr__(self):
        return '->'.join(str(r) for r in self.route)
