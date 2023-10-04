import math

def test_quiz():

    grade = 50
    assert grade >= 50

def test_temperature():
    celcius = 20
    fahrenheit = 35

    assert celcius + fahrenheit == 55

def test_area():
    square = 4

    assert square*square == 16
