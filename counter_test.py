import pytest
from counter import read_file
from counter import count_total_cars
from counter import count_daily_cars
from counter import count_most_cars

# expected data used in these tests here is from traffic.log
LOG_FILE = read_file('traffic.log')

"""We know the total number contained in traffic.log so this is pretty easy.
"""
def test_count_total_cars(input=LOG_FILE):

	expected = 398
	actual = count_total_cars(input)

	assert expected == actual,"test passed"

"""Check we are outputting the correct counts for daily totals
"""
def test_count_daily_cars(input=LOG_FILE):
	expected = {'2016-12-01': 179, '2016-12-05': 81, '2016-12-08': 134, '2016-12-09': 4}
	actual = count_daily_cars(input)

	assert expected == actual, "test passed"

"""We only care about the top 3 values here
"""
def test_count_most_cars(input=LOG_FILE):
	expected = ['2016-12-01T07:30:00 46', '2016-12-01T08:00:00 42', '2016-12-08T18:00:00 33']
	actual = count_most_cars(input)

	assert expected == actual

def test_count_least_cars(input=LOG_FILE):
	expected = 0


# def test_file1_method2():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed" 