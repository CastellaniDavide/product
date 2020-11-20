"""Test product file
"""
from product import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-11-20"

def test():
	"""Tests the product function in the product class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert product.product() == "product", "test failed"
	#assert product.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
