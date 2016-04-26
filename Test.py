from numpy.random import *
import matplotlib.pyplot as plt

def dice():
    return randint(1,7)

data = []
for x in range(10000):
    count = 1
    while dice() != 3:
        count += 1
    data.append( count )

#print data

plt.hist(data, bins=133)
plt.show()
