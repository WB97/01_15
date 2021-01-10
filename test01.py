import csv
with open('seoul.csv') as f:
    data = csv.reader(f)
    header = next(data)
    hdata = ['',0]
    for row in data:
        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])
        if row[4] > hdata[1]:
            hdata[0] = row[2]
            hdata[1] = row[4]
    print(hdata)