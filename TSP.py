import math
import sys

import numpy as np
import numpy.random as rn

interval = (-10, 10)


def f(x):
    """ Function to minimize."""
    global distance
    cost = 0

    for i in range(0,len(x)-1):
        cost  = cost + np.array(distance)[x[i], x[i+1]]
    return cost

def clip(x):
    """ Force x to be in the interval."""
    a, b = interval
    return np.max(np.min(x, b), a)

def random_start():
    """ Random point in the interval."""
    global k
    ans = []
    ans.append(0)
    ans.extend(np.random.choice(range(1, k), k-1, replace=False))
    ans.append(0)
    return ans

def cost_function(x):
    """ Cost of x = f(x)."""
    return f(x)

def random_neighbour(x, k):
    """Move a little bit x, from the left or the right."""
    z = np.random.choice(range(1, k-2))
    temp = []
    for i in range(0, len(x)):
        if i == z:
            temp.append(x[i+1])
        elif i == z+1:
            temp.append(x[i-1])
        else:
            temp.append(x[i])
    return temp

def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        # print("    - Acceptance probabilty = 1 as new_cost = {} < cost = {}...".format(new_cost, cost))
        return 1
    else:
        p = np.exp(- (new_cost - cost) / temperature)
        # print("    - Acceptance probabilty = {:.3g}...".format(p))
        return p

def temperature(fraction):
    """ Example of temperature dicreasing as the process goes on."""
    q = 0.01
    w = 1
    if w < 1-fraction :
        return w
    elif q > 1- fraction :
        return q
    else :
        return 1-fraction




def annealing(maxsteps=1000):
    """ Optimize the black-box function 'cost_function' with the simulated annealing algorithm."""
    state = random_start()
    cost = cost_function(state)
    states, costs = [state], [cost]
    for step in range(maxsteps):
        fraction = step / float(maxsteps)
        T = temperature(fraction)
        new_state = random_neighbour(state, fraction)
        new_cost = cost_function(new_state)
        print("Step #{:>2}/{:>2} : T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}, new_state = {:>4.3g}, new_cost = {:>4.3g} ...".format(step, maxsteps, T, state, cost, new_state, new_cost))
        if acceptance_probability(cost, new_cost, T) > rn.random():
            state, cost = new_state, new_cost
            states.append(state)
            costs.append(cost)
    return state, cost_function(state), states, costs

k = 3
max = 20
distance = [[max,1,max,max],[1,max,1,max],[max,1,max,1],[max,max,1,max]]
annealing( maxsteps=30)