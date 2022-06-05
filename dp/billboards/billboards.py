import math
import os
import random
import re
import sys

def find_buddies(x, D):
    buddy = [-1 for i in range(len(x))]
    right = len(x) - 1
    left = len(x) - 1
    while (right >= 0):
        if (left < 0):
            buddy[right] = -1
            right -= 1
            left = right
        elif (x[right] - x[left]) >= D:
            buddy[right] = left
            right -= 1
            left = right
        else:
            left -= 1
    
    return buddy

def billboards(D, x, v):
    # preprocess buddies    
    buddy = find_buddies(x, D)
    
    # initialize best array
    best = [0 for i in range(len(x))]
    best[0] = v[0]
    choices = []
    
    # compute best array using DP equation
    for i in range(1, len(x)):
        if (buddy[i] == -1):
            best[i] = max(best[i-1], v[i])
        else:
            best[i] = max(best[i-1], v[i] + best[buddy[i]])
    
    # backtrack to get choices that led to optimal path
    i = len(x) - 1
    while (i >= 0):
        if (i != 0 and best[i] == best[i-1]):
            i -= 1
            continue
        else:
            choices.append(i+1)
            i = buddy[i]
    
    print(best[-1])
    [print(i, end = " ") for i in choices]

if __name__ == '__main__':
    D = int(input().strip())

    xi = list(map(int, input().rstrip().split()))

    vi = list(map(int, input().rstrip().split()))
    
    billboards(D, xi, vi)