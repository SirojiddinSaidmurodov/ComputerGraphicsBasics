import numpy as np
import math


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.axes = np.array([x, y, z, 1])

    def set_point(self, arr):
        self.axes = arr
        self.x = arr[0]
        self.y = arr[1]
        self.z = arr[2]

    def turn(self, rx, ry, rz):
        rxRad = math.radians(rx)
        ryRad = math.radians(ry)
        rzRad = math.radians(rz)
        Rx = np.array([[1, 0, 0, 0],
                       [0, math.cos(rxRad), math.sin(rxRad), 0],
                       [0, -math.sin(rxRad), math.cos(rxRad), 0],
                       [0, 0, 0, 1]])
        Ry = np.array([[math.cos(ryRad), 0, -math.sin(ryRad), 0],
                       [0, 1, 0, 0],
                       [math.sin(ryRad), 0, math.cos(ryRad), 0],
                       [0, 0, 0, 1]])
        Rz = np.array([[math.cos(rzRad), math.sin(rzRad), 0, 0],
                       [-math.sin(rzRad), math.cos(rzRad), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
        temp = self.axes
        self.set_point(temp @ Rx @ Ry @ Rz)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return str(self.x) + "-" + str(self.y) + "-" + str(self.z)


class Sphere:
    def __init__(self, center: Point3D, radius, angle: Point3D = Point3D(0, 0, 0)):
        self.center = center
        self.radius = radius
        self.angle = angle

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
        for i in range(longitude_count - 1):
            for j in range(latitude_count - 1):
                lines.append((Point3D(x[i, j], y[i, j], z[i, j]), Point3D(x[i + 1, j], y[i + 1, j], z[i + 1, j])))
                lines.append((Point3D(x[i, j], y[i, j], z[i, j]), Point3D(x[i, j + 1], y[i, j + 1], z[i, j + 1])))
        #  turning points
        for line in lines:
            b, e = line
            b.turn(self.angle.x, self.angle.y, self.angle.z)
            e.turn(self.angle.x, self.angle.y, self.angle.z)

        # TODO: delete invisible lines
        # TODO: set a point of view
        return lines
