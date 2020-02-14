"""
Vectors for storing coordinates
"""

from math import cos, sin, radians, sqrt


class Vector3(object):
    """
    Holds a x, y, z
    """
    def __init__(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z

    @staticmethod
    def dist_points(point_1: "Vector3", point_2: "Vector3") -> float:
        x = pow(point_1.x - point_2.x, 2)
        y = pow(point_1.y - point_2.y, 2)
        z = pow(point_1.z - point_2.z, 2)
        return sqrt(x + y + z)

    def rotate_side(self, rotation: int, rounding: int = 5):
        """
        Rotate the vector along xy
        :return:
        """
        # print(f"moving upp and down by {rotation} degrees")
        rotation = radians(rotation)
        new_x = self.x*cos(rotation) - self.y*sin(rotation)
        new_y = self.x*sin(rotation) + self.y*cos(rotation)
        self.x, self.y = round(new_x, rounding), round(new_y, rounding)

    def rotate_upp_and_down(self, rotation: int, rounding: int = 5):
        """
        Rotate the vector along yz
        :return:
        """
        rotation = radians(rotation)
        new_x = self.x * cos(rotation) - self.z * sin(rotation)
        new_z = self.x * sin(rotation) + self.z * cos(rotation)
        self.x, self.z = round(new_x, rounding), round(new_z, rounding)

    def set_length(self, length: float):
        old_length = self.length
        self.x = (self.x / old_length) * length
        self.y = (self.y / old_length) * length
        self.z = (self.z / old_length) * length

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    @property
    def length(self):
        return self.dist_points(Vector3(0, 0, 0), self)

    def __add__(self, other: "Vector3"):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)

    def __iadd__(self, other):
        new = self + other
        self.x, self.y, self.z = new.x, new.y, new.z
        return self


class _Vector2(object):
    """
    Just for internal use, holds a x and y
    """
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
