import numpy as np
import math


class Point3D:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.axes = coordinates

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return str(self.x) + "-" + str(self.y) + "-" + str(self.z)


class Sphere:
    def __init__(self, center: Point3D, radius, angle: Point3D = Point3D(np.array([0, 0, 0, 1]))):
        self.center = center
        self.radius = radius
        self.angle = Point3D(np.radians(angle.axes))

    def __get_coord(self, lat: float, long: float) -> Point3D:
        return Point3D(np.array([self.radius * math.cos(math.radians(lat)) * math.sin(math.radians(long)),
                                 self.radius * math.cos(math.radians(lat)) * math.cos(math.radians(long)),
                                 self.radius * math.sin(math.radians(lat)),
                                 1]))

    def rotate(self, points_matrix, rx, ry, rz):
        Rx = np.array([[1, 0, 0, 0],
                       [0, math.cos(rx), math.sin(rx), 0],
                       [0, -math.sin(rx), math.cos(rx), 0],
                       [0, 0, 0, 1]])
        Ry = np.array([[math.cos(ry), 0, -math.sin(ry), 0],
                       [0, 1, 0, 0],
                       [math.sin(ry), 0, math.cos(ry), 0],
                       [0, 0, 0, 1]])
        Rz = np.array([[math.cos(rz), math.sin(rz), 0, 0],
                       [-math.sin(rz), math.cos(rz), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
        rot_matrix = Rx @ Ry @ Rz
        _, a, b = points_matrix.shape
        for i in range(a):
            points_matrix[:, i, :] = points_matrix[:, i, :] @ rot_matrix
        return points_matrix

    def get_points(self, longitude_count: int, latitude_count: int) -> list:
        u, v = np.mgrid[0:2 * np.pi:complex(longitude_count), 0:np.pi:complex(latitude_count)]
        x = np.cos(u) * np.sin(v) * self.radius
        y = np.sin(u) * np.sin(v) * self.radius
        z = np.cos(v) * self.radius
        points = np.stack((x, y, z, np.ones(x.shape)))
        #  rotating points, transposing points matrix for correct matrix product
        self.rotate(points.T, self.angle.x, self.angle.y, self.angle.z)
        #  filling lines list
        lines = []
        for i in range(longitude_count - 1):
            for j in range(latitude_count - 1):
                #  All lines are visible by default
                lines.append((Point3D(points[:, i, j]),
                              Point3D(points[:, i + 1, j]),
                              0))
                lines.append((Point3D(points[:, i, j]),
                              Point3D(points[:, i, j + 1]),
                              0))

        #  TODO: delete invisible lines
        #  TODO: set a point of view
        return lines
