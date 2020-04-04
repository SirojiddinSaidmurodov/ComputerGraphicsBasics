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

    def get_points(self, longitude_count: int, latitude_count: int) -> list:
        lines = []
        u, v = np.mgrid[0:2 * np.pi:complex(longitude_count), 0:np.pi:complex(latitude_count)]
        x = np.cos(u) * np.sin(v) * self.radius
        y = np.sin(u) * np.sin(v) * self.radius
        z = np.cos(v) * self.radius
        x += 250
        y += 250
        z += 250
        for i in range(longitude_count - 1):
            for j in range(latitude_count - 1):
                lines.append((Point3D(x[i, j], y[i, j], z[i, j]), Point3D(x[i + 1, j], y[i + 1, j], z[i + 1, j])))
                lines.append((Point3D(x[i, j], y[i, j], z[i, j]), Point3D(x[i, j + 1], y[i, j + 1], z[i, j + 1])))
        return lines
