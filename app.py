import numpy as np
import matplotlib.pyplot as mtplt
import random
from sortMethod import *

cluster = []

desiredLength = 50

while len(cluster) < desiredLength:
    number = random.randint(1, desiredLength)

    if not cluster:
        cluster.append(number)

    else:
        # Check exisiting number in cluster
        for index in range(len(cluster)):
            if number not in cluster:
                cluster.append(number)
                break
            else:
                continue

print('Unsorted number: '+str(cluster))

print('What sort you wanted :')
print('1.)Selection sort')
print('2.)Bubble sort')

userInput = input()

if userInput == '1':
    result, totalLoop = selectionSort(cluster)
    print('sort result: '+str(result))
    print('total Loop: '+str(totalLoop))

else:
    result, totalLoop = bubbleSort(cluster)
    print('sort result: '+str(result))
    print('total Loop: '+str(totalLoop))
