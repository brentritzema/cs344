"""
This module implements local search on a traveling salesman problem variant.
This structure is mostly copied from the queens.py problem given by kvlinden in CS344.

@author: brentritzema
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule
from random import randrange
import itertools


class TSPVariant(Problem):
    def __init__(self, initial):
        """Takes the inital path and calculates how many cities it needs to visit"""
        self.n = len(initial)
        self.initial = initial

    def actions(self, state):
        """Actions move the salesman to a city he hasn't been to before, if none exist,
           he returns home. Distance is added for each move. I won't swap the start and end A's
           because the distance should be the same no matter which city you start with since
           all the cities are interconnected.
        """
        actions = []
        # only swap the inner cities, not the outer cities because it reduces the search space and which city
        # you start at doesn't effect the problem since all cities are interconnected
        for permutation in range(1, 10):
            i = randrange(1, self.n-1)
            j = randrange(1, self.n-1)
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]
            actions.append(new_state)
        return actions

    def result(self, state, action):
        """Makes the given move on a copy of the given state."""
        return action

    def goal_test(self, state):
        """Check to see if there are no conflicts."""
        return not self.conflicted(state)

    def conflicted(self, state):
        # check if the beginning and end match
        if state[0] != state[len(state)-1]:
            return True

        # check if the state ended as the right length
        if len(state) != self.n:
            return True

        # check if the city has already been seen
        visited = []
        for city in self.initial:
            if city in visited and city != self.initial[0]:
                return True
            visited.append(city)
            if city not in state:
                return True

        return False

    def value(self, state):
        """This method computes a value of given state based on the connection distances between cities.
        """

        value = 0
        for i in range(0, self.n-1):
            value -= connections[(state[i], state[i+1])]

        return value


if __name__ == '__main__':

    n = 1000
    cities = []
    for i in range(0, n):
        cities.append("City" + str(i))

    connections = {}
    for permutation in list(itertools.permutations(cities, 2)):
        # doubling the amount of work I actually need to do to make things symmetrical
        # because this is the easiest way I can think of doing it
        distance = randrange(1, 100)
        connections[(permutation[1], permutation[0])] = distance
        connections[permutation] = distance

    initial = cities[:]
    initial.append(cities[0])

    # start and end must be the same, no city must appear twice except for the start and end point
    # initial = ["A", "B", "C", "D", "E", "A"]
    # connections = {
    #     ("A", "B"): 5,
    #     ("A", "C"): 100,
    #     ("A", "D"): 15,
    #     ("A", "E"): 25,
    #     ("B", "C"): 2,
    #     ("B", "D"): 10,
    #     ("B", "E"): 15,
    #     ("C", "D"): 7,
    #     ("C", "E"): 10,
    #     ("D", "E"): 13
    # }
    # symmetrical_connections = {}
    # for path in connections.keys():
    #     symmetrical_connections[path[1], path[0]] = connections[path];
    #
    # connections.update(symmetrical_connections)

    # Formulate a problem with a 2D hill function and a single maximum value.
    p = TSPVariant(initial)
    print('Initial: ')
    print('\tPath:  ' + str(initial))
    print('\tValue: ' + str(-1*p.value(initial)))

    # # Solve the problem using hill-climbing.
    # Solve the problem using hill climbing.
    hill_solution = hill_climbing(p)
    print('Hill-climbing:')
    print('\tSolution: ' + str(hill_solution))
    print('\tValue:    ' + str(-1*p.value(hill_solution)))
    print('\tGoal?     ' + str(p.goal_test(hill_solution)))

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    print('Simulated annealing:')
    print('\tSolution: ' + str(annealing_solution))
    print('\tValue:    ' + str(-1*p.value(annealing_solution)))
    print('\tGoal?     ' + str(p.goal_test(annealing_solution)))

