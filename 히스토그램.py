import matplotlib.pyplot as plt
#
# plt.hist([1,1,2,3,4,5,6,6,7,8,10])
#
# plt.show()

# import random
# dice = []
# for i in range(5):
#     dice.append(random.randint(1,6))
# plt.hist(dice, bins=6)
# print(dice)
# plt.show()

import csv

with open('seoul.csv') as f:
    data = csv.reader(f)
    next(data)
    result = []

    for row in data:
        if row[-1] != '':
            result.append(float(row[-1]))

plt.hist(result, bins=100, color='r')
plt.show()