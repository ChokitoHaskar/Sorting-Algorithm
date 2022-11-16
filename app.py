import os
import numpy as np
import matplotlib.pyplot as mtplt
import random
from generator import numberGenerate
from sortMethod import *


# Check if input is not Integer
while True:
    numberLength = 0
    try:
        numberLength = int(
            input('Insert how many number you wanted to generate: '))
    except NameError and ValueError:
        print('Input must be a number')
    else:
        break

cluster = numberGenerate(numberLength)
textPath = 'result/SortingProcess.txt'

print('Unsorted number: '+str(cluster))

print('What sort you wanted :')
print('1.)Selection sort')
print('2.)Bubble sort')

userInput = input()

if userInput == '1':
    result, totalLoop, changeRecorded = selectionSort(cluster)
    if os.path.exists(textPath):
        textOpen = open(textPath, 'w')
        textOpen.write(str(changeRecorded))
    else:
        os.makedirs('result')
        textOpen = open(textPath, 'x')
        textOpen.write(str(changeRecorded))

    print('sort result: '+str(result))
    print('total Loop: '+str(totalLoop))
    print('Each Loops successfully recorded at {}'.format(textPath))

else:
    result, totalLoop, changeRecorded = bubbleSort(cluster)
    if os.path.exists(textPath):
        textOpen = open(textPath, 'w')
        textOpen.write(str(changeRecorded))
    else:
        os.makedirs('result')
        textOpen = open(textPath, 'x')
        textOpen.write(str(changeRecorded))

    print('sort result: '+str(result))
    print('total Loop: '+str(totalLoop))
    print('Each Loops successfully recorded at {}'.format(textPath))
