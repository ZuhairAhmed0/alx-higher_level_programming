#!/usr/bin/python3
def roman_to_int(roman_string):
	if roman_string is None:
		return 0
	"""
	units = list(range(0, 10))
	tens = list(range(10, 100, 10))
	hundreds = list(range(100, 1000, 100))
	thousands = list(range(1000, 4000, 1000))
	"""
	units = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
	tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
	handreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
	thundreds = ["M", "MM", "MMM"]

	return matched
