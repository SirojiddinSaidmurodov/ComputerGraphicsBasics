import numpy as np
import math


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.axes = np.array([x, y, z])

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return str(self.x) + "-" + str(self.y) + "-" + str(self.z)


class Sphere:
    def __init__(self, center: Point3D, radius):
        self.center = center
        self.radius = radius

    def __get_coord(self, lat: float, long: float) -> Point3D:
        return Point3D(self.radius * math.cos(math.radians(lat)) * math.sin(math.radians(long)),
                       self.radius * math.cos(math.radians(lat)) * math.cos(math.radians(long)),
                       self.radius * math.sin(math.radians(lat)))

    def get_points(self, B: int, L: int) -> list:
        lines = []
        poles = [self.__get_coord(90, 0), self.__get_coord(-90, 0)]
        level = [poles[0]] * L
        latitudes = [90 - (180 / B) * k for k in range(1, B + 1)]
        longs = [(360 / L) * k for k in range(L)]
        temp = []
        for i in range(len(latitudes)):
            for j in range(len(longs)):
                temp.append(self.__get_coord(i, longs[j]))  # next level
                lines.append((level[j], temp[j]))  # lines from current level to the next one
            if i != B - 1:  # if the next level is not pole
                for j in range(L):
                    if j == L - 1:
                        next_point = 0
                    else:
                        next_point = j + 1
                    lines.append((temp[j], temp[next_point]))  # lines between points of one level
            level = temp  # change next level
            temp.clear()
        return lines
