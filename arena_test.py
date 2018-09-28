import pytest
import superheroes
# from superheroes import *
import random
import io
import sys



# Helper Functions
def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()

def test_apple():
    hero = superheroes.Hero("hero")
    apple = hero.apple()
    assert apple == 4

def test_orange():
    fruit = superheroes.orange()
    assert fruit == 4
