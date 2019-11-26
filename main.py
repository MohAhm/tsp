from genetic_algorithm import GeneticAlgorithm
from city import City
from route import Route


data = [
    (565.0, 575.0), (25.0, 185.0),
    (345.0, 750.0), (945.0, 685.0),
    (845.0, 655.0), (880.0, 660.0)
]


def main():
    """ EntryPoint """

    # 1 Create list of cities
    cities = []
    for i, axis in enumerate(data, 1):
        cities.append(City(i, axis[0], axis[1]))

    # print(cities[1].x, cities[1].y)

    # 2 Create GA object
    ga = GeneticAlgorithm(50, 0.01, 0.8, 0)

    # 3 Initialize population
    initial_population = ga.init_population(len(data))
    for individual in initial_population.population:
        route = Route(individual, cities)
        print('Route: ', route)


if __name__ == '__main__':
    main()
