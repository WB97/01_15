import csv
import matplotlib.pyplot as plt

# def show_age(a):
#     with open('age.csv') as f:
#         data = csv.reader(f)
#         result = []
#
#         # for row in data:
#         #     if '4719056500' in row[0]:
#         #         for i in enumerate(row[3:]):
#         #             print(i)
#
#     #     for row in data:
#     #         if a in row[0]:
#     #             for i in row[3:]:
#     #                 result.append(int(i))
#     # plt.rc('font', family = 'Malgun Gothic')
#     # plt.title(f'{a} 지역의 인구 구조')
#     # plt.plot(result)
#     # plt.show()
#
#     #     for row in data:
#     #         if a in row[0]:
#     #             for i in row[3:]:
#     #                 result.append(int(i))
#     # plt.rc('font', family = 'Malgun Gothic')
#     # plt.title(f'{a} 지역의 인구 구조')
#     # plt.barh(range(len(result)),result)
#     # plt.show()
#
#

with open('gender.csv') as f:
    data = csv.reader(f)
    m = []
    f = []

    for row in data:
        if '(5011000000)' in row[0]:
            for i in range(101):
                # m.append(int(row[i+3]))
                # f.append(-int(row[-(i + 1)]))
                m.append(int(row[i + 3].replace(',', '')))
                f.append(int(row[-(i + 1)].replace(',', '')))
    f.reverse()
plt.barh(range(101),m)
plt.barh(range(101),f)
plt.show()

# a = input('찾을 주소 입력 : ')
# show_age(a)

# a = ['경상북도 구미시 봉곡동', 123, 'ㅁㄴㅇ']
# if a[0].split(' ')[1] == '구미시':
#     print(a[0])