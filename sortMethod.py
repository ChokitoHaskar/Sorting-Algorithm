def selectionSort(data):
    loop = 0
    index = 0
    changeRecorded = ''

    while index < len(data):
        loop += 1
        minimumIndex = index
        comparedIndex = index + 1
        while comparedIndex < len(data):
            loop += 1
            if data[comparedIndex] < data[minimumIndex]:
                data[minimumIndex], data[comparedIndex] = data[comparedIndex], data[minimumIndex]
                changeRecorded += str(data) + '\n'
            comparedIndex += 1
        index += 1

    result = data
    totalLoop = loop

    return result, totalLoop, changeRecorded


def bubbleSort(data):
    loop = 0
    changeRecorded = ''

    for i in range(len(data)):
        loop += 1
        index = 0
        firstIndex = 0
        secondIndex = firstIndex + 1
        while index < len(data)-1:
            loop += 1
            if data[firstIndex] > data[secondIndex]:
                data[firstIndex], data[secondIndex] = data[secondIndex], data[firstIndex]
                changeRecorded += str(data) + '\n'
            firstIndex = secondIndex
            secondIndex += 1
            index += 1

    result = data
    totalLoop = loop

    return result, totalLoop, changeRecorded
