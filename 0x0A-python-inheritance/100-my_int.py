#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Override == operator with != behavior"""
        return not self.value == other

    def __ne__(self, other):
        """Override != operator with == behavior"""
        return not self.value != other
