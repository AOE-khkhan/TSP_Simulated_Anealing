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

def random_neighbour(x):
    """Move a little bit x, from the left or the right."""
    global k
    z = np.random.choice(range(1, int(k-1)),1)
    z = z[0]
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
    p=0
    if new_cost < cost:
        p=1
    else:
        # p = np.exp(- (new_cost - cost) / temperature)
        p= temperature
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
        new_state = random_neighbour(state)
        new_cost = cost_function(new_state)
        print('Step '+str(step)+' : T = '+str(round(T,2))+' state = '+str(state)+' cost = '+str(cost)+' new_state = '+str(new_state)+' new_cost = '+str(new_cost))
        if acceptance_probability(cost, new_cost, T) > rn.random():
            state, cost = new_state, new_cost
            states.append(state)
            costs.append(cost)
    return state, cost_function(state), states, costs

k = 4
max = 1000
distance = [[max,1,max,max],[1,max,1,max],[max,1,max,1],[max,max,1,max]]
annealing( maxsteps=30)