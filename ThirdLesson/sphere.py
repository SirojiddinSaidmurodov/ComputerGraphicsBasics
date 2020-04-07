import numpy as np
import math


class Point3D:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.axes = coordinates

    def __eq__(self, other):
        if (self.axes == other.axes).sum() == 4:
            return True
        return False

    def __str__(self):
        return str(self.x) + "-" + str(self.y) + "-" + str(self.z)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.visibility = 0

    def to_tuple(self):
        return self.p1, self.p2, self.visibility

    def set_v(self):
        self.visibility += 1

    def __eq__(self, other):
        if self.p1 == other.p2 and self.p2 == other.p2 or self.p1 == other.p2 and self.p2 == self.p1:
            return True
        return False


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
                lines.append(Line(Point3D(points[:, i, j]),
                                  Point3D(points[:, i + 1, j])))
                lines.append(Line(Point3D(points[:, i, j]),
                                  Point3D(points[:, i, j + 1])))

        #  delete invisible lines using Roberts algorithm
        for i in range(longitude_count - 1):
            for j in range(1, latitude_count - 1):
                if i == 0:
                    temp = [points[:, i, j - 1],
                            points[:, i + 1, j],
                            points[:, i, j + 1]]
                else:
                    temp = [points[:, i - 1, j],
                            points[:, i, j - 1],
                            points[:, i + 1, j],
                            points[:, i, j + 1],
                            points[:, i - 1, j]]
                for surface in range(len(temp) - 1):
                    v1 = temp[surface] - points[:, i, j]
                    v2 = temp[surface + 1] - points[:, i, j]
                    A = v1[1] * v2[2] - v2[1] * v1[2]
                    B = v1[2] * v2[0] - v2[2] * v1[0]
                    C = v1[0] * v2[1] - v2[0] * v1[1]
                    D = -(A * v1[0] + B * v1[1] + C * v1[2])
                    #  if (A·W.X + B·W.Y + C·W.Z + D)<0 : but W is (0,0,0)
                    if D < 0:
                        m = -1
                    else:
                        m = 1
                    #  correcting surface normal vector
                    A, B, C, D = A * m, B * m, C * m, D * m



        return lines
