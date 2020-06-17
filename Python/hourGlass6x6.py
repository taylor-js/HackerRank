import math
import os
import random
import re
import sys

def hourGlass6x6(mtx):
    arr = []
    dt = {}
    for i in range(len(mtx)):
        for j in range(i):
            dt.setdefault(i,sum(mtx[i][j:j+3]))
    return dt

mtx = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
print(hourGlass6x6(mtx))