import math

import numpy as np


def roberts(points, point_of_view):
    points.append(points[0])
    a, b, c = 0, 0, 0
    for i in range(len(points) - 1):
        a += (points[i][1] - points[i + 1][1]) * (points[i][2] + points[i + 1][2])
        b += (points[i][2] - points[i + 1][2]) * (points[i][0] + points[i + 1][0])
        c += (points[i][0] - points[i + 1][0]) * (points[i][1] + points[i + 1][1])
    d = -(a * points[0][0] + b * points[0][1] + c * points[0][2])
    if point_of_view[0] * a + point_of_view[1] * b + point_of_view[2] * c + point_of_view[3] * d < 0:
        return False
    return True


def rotate(points_matrix, rx, ry, rz):
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


class Cylinder:
    def __init__(self, center, radius, hight, angle=(np.array([0, 0, 0, 1]))):
        self.center = center
        self.radius = radius
        self.hight = hight
        self.angle = np.radians(angle)

    def get_lines(self, longitude_count: int, latitude_count: int):
        u, v = np.mgrid[0:2 * np.pi:complex(longitude_count), 0:np.pi:complex(latitude_count - 2)]
        x = np.cos(u) * self.radius
        x = np.hstack((np.zeros((longitude_count, 1)), x, np.zeros((longitude_count, 1))))
        y = np.sin(u) * self.radius
        y = np.hstack((np.zeros((longitude_count, 1)), y, np.zeros((longitude_count, 1))))
        z = np.array(
            [[self.hight * (i / (latitude_count - 2)) for i in range(latitude_count - 2)] for t in
             range(longitude_count)])
        z = np.hstack((np.zeros((longitude_count, 1)), z,
                       np.ones((longitude_count, 1)) * self.hight * (latitude_count - 3) / (latitude_count - 2)))
        points = np.stack((x, y, z, np.ones(x.shape)))
        #  rotating points, transposing points matrix for correct matrix product
        points = points.T
        rotate(points, self.angle[0], self.angle[1], self.angle[2])
        #  filling lines list
        lines = []
        for i in range(longitude_count - 1):
            for j in range(latitude_count - 1):
                #  All lines are visible by default
                if roberts([points[j, i, :].tolist(), points[j, i + 1, :].tolist(),
                            points[j + 1, i + 1, :].tolist(), points[j + 1, i, :].tolist()],
                           [0, 0, -1, 0]):
                    lines.append((points[j, i, :], points[j, i + 1, :]))
                    lines.append((points[j, i, :], points[j + 1, i, :]))
            #  delete invisible lines using Roberts algorithm
        return lines
