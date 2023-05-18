import copy

import numpy as np
import random

n = 16


def Conflicts(var, v, csp):
    row = copy.deepcopy(csp[v])
    conflicts = np.sum(row, axis=0, keepdims=False) - 1

    i = v + 1
    j = var + 1
    while i < n and j < n:
        if csp[i][j] == 1:
            conflicts += 1
        i += 1
        j += 1

    i = v - 1
    j = var - 1
    while i >= 0 and j >= 0:
        if csp[i][j] == 1:
            conflicts += 1
        i -= 1
        j -= 1

    i = v + 1
    j = var - 1
    while i < n and j >= 0:
        if csp[i][j] == 1:
            conflicts += 1
        i += 1
        j -= 1

    i = v - 1
    j = var + 1
    while i >= 0 and j < n:
        if csp[i][j] == 1:
            conflicts += 1
        i -= 1
        j += 1
    return conflicts


def Initialize():
    csp = np.zeros((n, n))
    for i in range(n):
        v = random.randint(0, n - 1)
        csp[v][i] = 1
    return csp


def Solution(csp):
    for i in range(n):
        for j in range(n):
            if csp[i][j] == 1 and Conflicts(j, i, csp) != 0:
                return False
    return True


def ConflictedVariables(csp):
    variables = []
    for i in range(n):
        for j in range(n):
            if csp[j][i] == 1:
                if Conflicts(i, j, csp) != 0:
                    variables.append(i)
    return variables


def MinConflicts(max_steps):
    csp = Initialize()

    for i in range(max_steps):

        if Solution(csp):
            return csp

        variables = ConflictedVariables(csp)
        var = variables[random.randint(0, len(variables) - 1)]

        minimum_conflicts = np.inf
        csp[:, var] = 0
        v = -1
        for j in range(n):
            conflicts = Conflicts(var, j, csp)
            if conflicts < minimum_conflicts:
                minimum_conflicts = conflicts
                v = j
        csp[v][var] = 1
    return None


if __name__ == '__main__':
    eight_queens = MinConflicts(1000)
    if eight_queens is None:
        print("failure")
    else:
        print(eight_queens)
