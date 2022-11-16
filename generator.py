import random


def numberGenerate(desiredLength):
    cluster = []

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

    return cluster
