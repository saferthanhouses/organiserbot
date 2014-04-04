from nose.tools import *
from OrganiserBot import organiser_bot
import fixtures

def setup():
	print("SETUP!")

def teardown():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN")


class SomethingTest:
	def test(self):
		assert 0