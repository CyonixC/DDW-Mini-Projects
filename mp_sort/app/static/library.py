from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	arr = []
	for _ in range(number):
		arr.append(random.randint(0,10))
	return arr

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	arr = gen_random_int(number,seed)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = ", ".join([str(num) for num in arr])
	array_str += "."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

	array_str = document.getElementById("generate").innerHTML
	array = array_str[:-1].split(", ")
	array = [int(num) for num in array]
	for outer in range(1,len(array)):
		for inner in range(outer, 0 , -1):
			if array[inner] < array[inner - 1]:
				array[inner], array[inner - 1] = array[inner- 1], array[inner]
	array_str = ", ".join([str(num) for num in array])
	array_str += "."

	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	value = "".join(value.split())
	array = value.split(",")
	try:
		array = [float(val) for val in array]
	except:
		window.alert("Your input contains non-numbers!")
		return
	for outer in range(1,len(array)):
		for inner in range(outer, 0 , -1):
			if array[inner] < array[inner - 1]:
				array[inner], array[inner - 1] = array[inner- 1], array[inner]

	array_str = ", ".join(array)
	array_str += "."

	document.getElementById("sorted").innerHTML = array_str


