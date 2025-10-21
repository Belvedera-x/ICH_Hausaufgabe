from simple_math import SimpleMath
import pytest


@pytest.fixture
def simplemath():
    return SimpleMath()


def test_square_positive(simplemath):
    assert simplemath.square(4) == 16


def test_square_negative(simplemath):
    assert simplemath.square(-6) == 36


def test_cube_positive(simplemath):
    assert simplemath.cube(4) == 64


def test_cube_negative(simplemath):
    assert simplemath.cube(-6) == -216