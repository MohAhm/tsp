from math import pow, sqrt


class City:
    def __init__(self, id, x, y):
        # Definition for cities coordinates
        self.id = id
        self.x = x
        self.y = y

    def distance_from(self, city):
        # Calculates the straight-line distance from the current city to another city
        delta_x = pow((city.x - self.x), 2)
        delta_y = pow((city.y - self.y), 2)

        distance = sqrt(delta_x + delta_y)
        return distance

    def __repr__(self):
        return "(%d)" % self.id
