"""
Classes for all objects
"""
from math import sqrt

from PyRay.color import Color
from .vector import Vector3


class _Object(object):
    def dist(self, point: Vector3) -> float:
        raise NotImplemented("Use a subclass of this")


class Sphere(_Object):
    def __init__(self, center: Vector3, radius: int, color: Color):
        self.center = center
        self.radius = radius
        self.color = color

    def dist(self, point: Vector3) -> float:
        return Vector3.dist_points(point, self.center) - self.radius