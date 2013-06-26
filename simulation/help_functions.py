__author__ = 'artyom'

import math


def getPermutation(l1, l2):
    perm_list = []
    permutation = map(dict((v, i) for i, v in enumerate(l1)).get, l2)
    for i in range(len(permutation)):
        j = i
        if permutation[j] == i:
            continue
        else:
            while permutation[j] != i:
                j += 1
            tupl = (i, j)
            perm_list.append(tupl)
            permutation[j] = permutation[i]
            permutation[i] = i
    return perm_list


def ellipsePerimeter(a, b):
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))


def idIsValid(robotId, robotsList):
    for i in range(len(robotsList)):
        if robotsList[i].id == robotId:
            return True
    return False


def idOnce(strIdList, robotId):
    count = 0
    for i in range(len(strIdList)):
        if strIdList[i] == robotId:
            count += 1
    return count == 1