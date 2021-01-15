import csv
import matplotlib.pyplot as plt

# size= [2441,2312,1031,1233]
# lable = ['A형','B형','AB형','O형']
# color = ['r','c','g','yellow']
#
# plt.rc('font', family='Malgun Gothic')
# plt.pie(size,labels=lable,autopct='%.1f%%', colors=color, explode=(0,0,0.1,0))
# plt.axis('equal')
# plt.legend()
# plt.show()

with open('gender.csv') as f:
    data = csv.reader(f)
    # m = 0
    # f = 0
    m = []
    f = []

    for row in data:
        if '(5011000000)' in row[0]:
            for i in range(101) :
                m.append(int(row[i+3].replace(',', '')))
                f.append(int(row[i+106].replace(',', '')))


# plt.pie([m,f], autopct='%.1f%%', startangle=45)
plt.plot(m)
plt.plot(f)
plt.show()