"""
Holds the Color class
"""

class Color:
    """
    Color class
    """

    # TODO: add rgb, hex, ect....

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name