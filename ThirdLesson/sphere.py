import numpy as np
import math
import cv2


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.axes = np.array([x, y, z])


class Vector:
    def __init__(self, x, y, z):
        a = max(x, y, z)
        self.x = x / a
        self.y = y / a
        self.z = z / a
        self.axes = np.array([self.x, self.y, self.z])


class Sphere:
    def __init__(self, center: Point3D, radius, angle: Vector):
        self.center = center
        self.radius = radius
        self.angle = angle

    def get_coord(self, lat: float, long: float) -> Point3D:
        return Point3D(self.radius * math.cos(math.radians(lat)) * math.sin(math.radians(long)),
                       self.radius * math.cos(math.radians(lat)) * math.cos(math.radians(long)),
                       self.radius * math.sin(math.radians(lat)))

    def get_points(self, B: int, L: int) -> list:
        lines = []
        poles = [self.get_coord(90, 0), self.get_coord(-90, 0)]
        level = [poles[0]] * L
        latitudes = [90 - (180 / B) * k for k in range(1, B + 1)]
        longs = [(360 / L) * k for k in range(L)]
        temp = []
        for i in range(len(latitudes)):
            for j in range(len(longs)):
                temp.append(self.get_coord(i, longs[j]))  # next level
                lines.append((level[j], temp[j]))  # lines from current level to the next one
            if i != B - 1:
                for j in range(L):
                    if j == L - 1:
                        next_point = 0
                    else:
                        next_point = j + 1
                    lines.append((temp[j], temp[next_point]))  # lines between points of one level
        return lines
