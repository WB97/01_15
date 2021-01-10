import csv
import matplotlib.pyplot as plt
# with open('seoul.csv') as f:
#     data = csv.reader(f)
#     next(data)
#     result = []
#     high = []
#     low = []
#     for row in data:
#         if row[3] != '' and row[4] != '':
#             if int(row[0].split('-')[0]) >= 1983:
#                 if row[0].split ('-')[1] == '02' and row[0].split('-')[2] == '14' :
#                     high.append(float(row[3]))
#                     low.append(float(row[4]))
#
# plt.figure(figsize = (10,4))
# plt.plot(high,'r')
# plt.plot(low,'b')
# plt.show()

with open('seoul.csv') as f:
    data = csv.reader(f)
    next(data)
    # high = []
    # low = []
    a=[]
    b=[]
    for row in data:
        if row[3] != '' and row[4] != '':
            if int(row[0].split('-')[0]) >= 1908:
                if row[0].split('-')[1] == '05' and row[0].split('-')[2] == '21' :
                    # high.append(float(row[4]))
                    # low.append(float(row[3]))
                    a.append((float(row[3])+float(row[4]))/2)
                    b.append(int(row[0].split('-')[0]))

print(a)
print(b)
plt.figure(figsize = (10,4))
# plt.plot(high,'r')
# plt.plot(low,'b')
plt.plot(b,a,'r')
plt.show()