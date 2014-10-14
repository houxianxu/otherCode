#!/usr/bin/python
# -*-coding:utf-8-*-

# Description: This script is an experiment to simulation Monty Hall problem, 
#              and the problem can be find http://en.wikipedia.org/wiki/Monty_Hall_problem
# Version: 1.0
# History: 2014-10-14 Created by Houxx

import random

# Choice for the problem
choice = ["Prize", None, None]

def solveMontyHall(num):
	""" Solve the Monty Hall problem by simulation
		Input: num -> the nubmer of Experiment
		Return: a tuple of two float value
			    the first one the probililty of insisting on the first choice
			    the second one is the probililty to switch to another
	"""

	# the number that the first choice is the anwser
	NumFirst = 0
	# the number that the switched choice is the anwser
	NumSwitch = 0

	for i in xrange(num):
		# Set randomly the index of the prize and first choice
		prizeIndex = random.randint(0, 2)
		firstChoiceIndex = random.randint(0, 2)

		# insist on the first choice 
		if firstChoiceIndex == prizeIndex:
			NumFirst += 1
		else: # failure
			pass

		# choose to switch 
		if firstChoiceIndex == prizeIndex:
			pass # failure
		else: # means you get the right answer
			NumSwitch += 1

	return (NumFirst / float(num), NumSwitch / float(num))

def main():
	# Number of Experiment
	N = 100000

	# the probililty to choose the first answer
	probFirstChoice, probSwitch = solveMontyHall(N)

	print 'The probility to insist the first choise is ' + str(probFirstChoice) + '\n'
	print 'The probililty to switch to another one is ' + str(probSwitch) + '\n'

if __name__ == '__main__':
	main()
