
from maim import *

assert 2+2 == 5, "wrong assert uslovie nepravilno"

def adder(*args, **kwargs):
result = 0
for _ in args:
result += _
for _ in kwargs.values():
result += _
return result