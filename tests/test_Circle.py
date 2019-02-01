"""
Contains tests for the circle section properties class
"""

from math import isclose

from BeamDesign.Sections.Circle import Circle
from BeamDesign.Materials.material import Steel

as3678_250 = Steel.load_steel(steel_name='AS3678-250')


def test_Circle():
    """
    Basic test of whether a circle can be initialised or not
    """

    c = Circle(radius=0.02, material=as3678_250)

    assert c


def test_Circle_is_circle():

    c = Circle(radius=0.02, material=as3678_250)

    assert c.is_circle


def test_Circle_is_hollow():

    c = Circle(radius=0.02, material=as3678_250)

    assert not c.is_hollow


def test_Circle_area():

    c = Circle(radius=0.02, material=as3678_250)

    actual = c.area
    expected = 0.00125663706143592

    assert isclose(actual, expected)
