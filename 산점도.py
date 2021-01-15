import csv
import matplotlib.pyplot as plt
import random
import math

x = []
y = []
size = []
a = []
#
# for i in range(100):
#     x.append(random.randint(50,100))
#     y.append(random.randint(50,100))
#     size.append(random.randint(10,100))

with open('gender.csv') as f:
    data = csv.reader(f)
    # m = 0
    # f = 0
    for row in data:
        if '(5000000000)' in row[0]:
            for i in range(3,104) :
                x.append(int(row[i].replace(',', '')))
                y.append(int(row[i+103].replace(',', '')))
                size.append(math.sqrt(int(row[i].replace(',', ''))+int(row[i+103].replace(',', ''))))

# plt.style.use('ggplot')
# plt.scatter(x,y, s=size, c=size, alpha=0.5)
# plt.colorbar()

plt.scatter(x,y, s=size, c=range(101), alpha=0.5, cmap='autumn')
plt.colorbar()
plt.plot(range(max(x)), range(max(x)))
print(max(y))
plt.show()