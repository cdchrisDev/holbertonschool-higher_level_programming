#!/usr/bin/python3
"""This is the 6-base_geometry
Module
"""


class BaseGeometry():
    """Defining basic geometry"""

    def area(self):
        """Basic area"""

        raise Exception("area() is not implemented")


if __name__ == '__main__':
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
