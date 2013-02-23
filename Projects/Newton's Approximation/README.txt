Newton's method for Successive Approximation
--------------------------------------------
Author: Karan Tamhane
Course: Introduction to Computer Science and Programming
School: MITx (edX)
Problem Set: 3

Summary:
	Implements Newton's method for successive approximation. Newton's method is used for estimating roots of a polynomial f(x). It is a guess and check method of approximation. Each successive guess is calculated by the given formula.

		x[n+1] = x[n] - f(x[n])/f'(x[n])

		x[n+1] => new guess
		x[n] => preveious guess

Source code: newton.py

Usage:
	
	Program must be run in a python shell.

	Call computeRoot(poly, x_0, epsilon)

	poly => given polynomial in form of a list of coefficients such that poly[i] is coefficient of x^i in the polynomial
	E.g. - If polynomial is x^2 + 5*x - 4 = 0, then poly = [-4, 5, 1] as coefficients of [x^0, x^1, x^2]
	
	x_0 => initial guess (float > 0)
	
	epsilon => error margin with which to estimate the root (float > 0)