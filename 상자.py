import matplotlib.pyplot as plt
import csv
#
# with open('seoul.csv') as f:
#     data = csv.reader(f)
#     next(data)
#     result = []
#
#     for row in data:
#         if row[-1] != '':
#             result.append(float(row[-1]))
#
# plt.boxplot(result)
# plt.show()


# with open('seoul.csv') as f:
#     data = csv.reader(f)
#     next(data)
#
#     month=[[],[],[],[],[],[],[],[],[],[],[],[]]
#
#     for row in data:
#         if row[-1] != '' :
#             month[int(row[0].split('-')[1])-1].append(float(row[-1]))
#
# plt.boxplot(month)
# plt.show()


# with open('seoul.csv') as f:
#     data = csv.reader(f)
#     next(data)
#
#     day = []
#     for i in range(31):
#         day.append([])
#
#     for row in data:
#         if row[-1] != '' :
#             if row[0].split('-')[1] == '08':
#                 day[int(row[0].split('-')[2])-1].append(float(row[-1]))
#
# plt.style.use('ggplot')
# plt.figure(figsize=(10,5),dpi=100)
# plt.boxplot(day,showfliers=True)
#
# plt.show()
