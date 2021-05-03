#!/usr/bin/env python3

"""
@author Isaac Keleher 2021
This is a series of unit testsfor our counter.py program
"""
import datetime
import pytest
from counter import count_most_cars
from counter import count_daily_cars
from counter import count_total_cars
from counter import count_least_cars
from counter import read_file

# expected data used in these tests here is from traffic.log
F_NAME = 'traffic.log'
LOG_FILE = read_file(F_NAME)


def test_read_file(input=F_NAME):
    """Check our file reading function
    Couldn't think of a whole lot to do for this one really.
    """
    actual = read_file(input)

    # check return type is valid list of tuples
    assert type(actual) is list, "test passed"
    assert actual is not None, "test passed"

    # check first and last items
    assert actual[0] is not None, "test passed"
    assert actual[-1] is not None, "test passed"
    assert type(actual[0]) is tuple, "test tupled"
    assert type(actual[-1]) is tuple, "test passed"


def test_count_total_cars(input=LOG_FILE):
    """Test func to count sum of all cars.

    We know the total number contained in traffic.log so this is pretty easy.
    """
    total_actual = count_total_cars(input)

    # check expected output
    expected = 398
    assert expected == total_actual, "test passed"

    # check expected data type
    assert type(total_actual) is int, "test passed"


def test_count_daily_cars(input=LOG_FILE):
    """Check we are outputting the correct counts for daily totals.
    """
    daily_actual = count_daily_cars(input)

    # Check expected output
    expected = {
        '2016-12-01': 179, '2016-12-05': 81, '2016-12-08': 134, '2016-12-09': 4
    }
    assert expected == daily_actual, "test passed"

    # Daily contains an int as the value
    for line in daily_actual:
        assert type(daily_actual[line]) is int, "test passed"

    # check daily count data is in YYYY-MM-DD
    for key in daily_actual:
        datetime.datetime.strptime(key, '%Y-%m-%d')
        with pytest.raises(ValueError):
            raise ValueError("incorrect data format, should be YYYY-MM-DD")


def test_count_most_cars(input=LOG_FILE):
    """We only care about the top 3 values here.
    """
    actual = count_most_cars(input)

    # check output matches expected
    expected = [
        '2016-12-01T07:30:00 46',
        '2016-12-01T08:00:00 42',
        '2016-12-08T18:00:00 33'
        ]
    assert expected == actual, "test passed"

    # check most_cars data is string
    for item in actual:
        assert type(item) is str, "test passed"

    # test sorting, we split the string and just check the numbers
    assert actual[0].split(' ')[1] > actual[2].split(' ')[1], "test passed"


def test_count_least_cars(input=LOG_FILE):
    """Check least_cars func with our pre-prepared answer.

    Better to do this with multiple sets of small and
    manually verifiable test data

    Note that test will break if you comment line 134
    in counter.py
    """
    actual = count_least_cars(input)

    # check expected output
    expected = '2016-12-05 11:00:00 7'
    assert expected == actual, "test passed"

    # check its a string
    assert type(actual) is str, "test passed"
