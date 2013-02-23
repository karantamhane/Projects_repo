# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    res = 0.0
    for ind in range(len(poly)):
        res += poly[ind]*(x**ind)
    return res



# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    res = []
    for ind in range(len(poly)):
        res.append(float(poly[ind]*ind))
    if len(res) > 1:
        res.remove(0)
    return res




# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    x = x_0
    iter = 0
    while abs(evaluatePoly(poly, x)) > epsilon:
        iter += 1
        x = x - (evaluatePoly(poly, x)/evaluatePoly(computeDeriv(poly), x))
    solution = [x, iter]
    return solution





    
