from random import random

from math import cos, sin


def complex_fi(fi):
    return complex(cos(fi), sin(fi))


def random_complex():
    fi = random()
    return complex_fi(fi)
