"""
Run the various CSP solvers on the class scheduling problem.
These calls are mostly copied/adapted from the zebra and nqueens solutions provided by kvlinden in CS344.

@author: brentritzema
"""

from csp import CSP, backtracking_search, min_conflicts, mrv, \
    forward_checking, AC3
from search import depth_first_graph_search
import itertools


def ClassSchedulingCSP():
    """Queens problem for the class scheduling problem. I've used the classes as the variables
    and combinations of time, professor, and classroom as the domains for each variable. The
    constraints are that no prof can teach two classes at the same time, no class can be in the
    same room at the same time as another class, and each course should be offered exactly once.
    """

    """Initialize data structures for the class scheduling problem."""
    classes = ['CS108', 'CS112', 'CS214', 'CS212', 'CS232', 'CS344']
    # classes = ['CS108', 'CS112']
    faculty = ['dschuurman', 'kvlinden', 'adams', 'norman']
    time_slots = ['mwf900', 'mwf1030', 'tth900', 'tth1030']
    classrooms = ['nh253', 'sb382']
    combination = [faculty, time_slots, classrooms]

    variables = classes
    domain = list(itertools.product(*combination))
    # for x in range(0, len(domain)):
    #     domain[x] = "_".join(str(i) for i in domain[x])
    domains = {}
    neighbors = {}
    for var in variables:
        domains[var] = domain
        neighbors[var] = [x for x in variables if x != var]

    def constraints(A, a, B, b):
        # a = a.split("_")
        # b = b.split("_")
        # check if it's the same time
        if a[1] == b[1]:
            # check if profs are the same
            if a[0] == b[0]:
                return False
            # check if rooms are the same
            elif a[2] == b[2]:
                return False
            else:
                return True
        else:
            return True

    return CSP(variables, domains, neighbors, constraints)


# 1. Set up the problem.
problem = ClassSchedulingCSP()

# 2. Solve the problem.

# solution = AC3(problem);
solution = backtracking_search(problem)
# solution = min_conflicts(problem)

# 3. Print the results.
# Handle AC3 solutions (boolean values) first, they behave differently.
if type(solution) is bool:
    if solution and problem.goal_test(problem.infer_assignment()):
        print('AC3 Solution:')
    else:
        print('AC Failure:')
    print(problem.curr_domains)

# Handle other solutions next.
elif solution != None and problem.goal_test(solution):
    print('Solution:')
    print(solution)
#    problem.display(problem.infer_assignment())
else:
    print('Failed - domains: ' + str(problem.curr_domains))
    problem.display(problem.infer_assignment())

