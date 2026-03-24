import pytest
import requests
from src.calculator import add, subtract, multiply, divide


# Replaces writing 4 identical test functions
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),        # positive
        (-1, 1, 0),       # negative
        (100, -50, 50),   # large values
    ],
)
def test_add_cases(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),        # positive
        (0, 0, 0),        # zeros
        (0, 1, -1),       # negative
        (50, -50, 100),   # large values
    ],
)
def test_subtract_cases(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),        # positive
        (0, 0, 0),        # zeros
        (-1, 1, -1),      # negative
        (100, 50, 5000),  # large values
    ],
)
def test_multiply_cases(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),        # positive
        (0, 0, 0),        # zeros
        (-2, 2, -1),      # negative
        (100, -50, -2),   # large values
    ],
)
def test_divide_cases(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.external
@pytest.mark.slow
def test_weather_api():
    resp = requests.get("https://api.github.com")
    assert resp.status_code == 200


@pytest.mark.skip(reason="WIP")
def test_not_ready():
    ...
