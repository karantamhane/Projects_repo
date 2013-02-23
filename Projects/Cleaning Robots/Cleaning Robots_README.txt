Cleaning Robots
---------------
Author: Karan Tamhane
Course: Introduction to Computer Science and Programming
School: MITx (edX)
Problem Set: 7

Summary:
	Runs a simulation to calculate cleaning time of a rectangular room by automatic cleaning robots. Cleaning time is estimated in arbitrary time units for relative comparison between different scenarios to optimize the cleaning process.
	Introduces robots into the room initially at random positions with random travel directions.
	
	StandardRobot => moves 'speed' number of distance units per unit time in a set direction till robot encounters edge of room. If at the edge of room, robot stops moving and only picks new random direction during that time step.

	RandomWalkRobot => moves 'speed' number of distance units per unit time in a set direction and also changes direction randomly at each time step. If at the edge of room, robot stops moving and only picks new random direction during that time step.

Source code: cleaning_robots.py

Modules imported:
	math, random, pylab

Usage:
	
	Program must be run in a python shell.

	Call runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type) to run simulation.

	num_robots => number of robots to be assigned to clean given room (int > 0).
	speed => cleaning speed of each robot in arbitrary units (float > 0.0)
	width => width of room floor (int > 0)
	height => height of room floor (int > 0)
	min_coverage => minimum fraction of room to be cleaned (0 <= float <= 1)
	num_trials => number of simulation trials (int > 0)
	robot_type => StandardRobot or RandomWalkRobot