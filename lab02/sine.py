"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden && bjr33
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class SineVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = SineVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    t0 = time.time()
    hill_solution = 0
    for i in range(1, 10):
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        hill_solution = max(hill_climbing(p), hill_solution)

    t1 = time.time()
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution)) + ' \ttime: ' + str(t1-t0)
          )

    # Solve the problem using simulated annealing.
    t2 = time.time()
    annealing_solution = 0
    for i in range(1, 10):
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        annealing_solution = max(simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        ), annealing_solution)
    t3 = time.time()
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution)) + '\ttime: ' + str(t3-t2)
          )
