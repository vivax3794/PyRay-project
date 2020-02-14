"""
The main world
"""
from copy import copy
from typing import Tuple

from .objects import _Object
from .vector import Vector3
from ._screen import Screen


class World(object):
    """
    The main world, holds all the objects.
    """

    def __init__(self,
                 width: int,
                 height: int,
                 camera: Vector3 = Vector3(0, 0, 0),
                 direction: Vector3 = Vector3(0, 0, 1),
                 curve: int = 0.01,
                 resolution: int = 1):

        self._screen = Screen(width, height)
        self._objects = []

        self._camera = camera
        self._camera_direction = direction
        self._camera_curve = curve
        self._resolution = resolution

    # should I move this to it's own file and/or class
    def _cast_ray(self, position: Vector3, direction: Vector3):
        position = copy(position)

        threshold = 0.01
        background_color = "white"
        background_threshold = 100

        while True:

            # find dist to nearest object
            dist = float("inf")
            closet_object = None
            for object_ in self._objects:
                dist_to_object = object_.dist(position)
                if dist_to_object < dist:
                    dist = dist_to_object
                    closet_object = object_

            if dist <= threshold:
                return closet_object.color
            elif dist >= background_threshold:
                return background_color
            else:
                # find how much to move
                direction.set_length(dist)
                position += direction

    def update(self):
        """
        Just a gate to Screen.update()
        :return:
        """
        print("casting rays")
        for x in range(0, self._screen.width, self._resolution):
            # print(x)
            for y in range(0, self._screen.height, self._resolution):
                # maybe this as a function? calculate_direction() maybe
                offset_x, offset_y = x - self._screen.width / 2, y - self._screen.height / 2
                direction = copy(self._camera_direction)
                direction.x = offset_x * self._camera_curve
                direction.y = offset_y * self._camera_curve
                direction.set_length(1)

                color = self._cast_ray(self._camera, direction)

                # scaling to fit screen
                for s_x in range(x, x + self._resolution):
                    for s_y in range(y, y + self._resolution):
                        self._screen.set_pixel(s_x, s_y, color)
        print("updating")
        self._screen.update()
        print("updating done")

    def add_object(self, object_: _Object):
        self._objects.append(object_)
