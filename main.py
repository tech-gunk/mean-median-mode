import csv
from collections import Counter

with open("height-weight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

def Mean():
    length = len(new_data)
    total = 0

    for i in new_data:
        total+=i

    mean = total/length
    print(mean)

def Median():
    l = len(new_data)
    new_data.sort()

    if (l%2 == 0):
        m1 = float(new_data[l//2])
        m2 = float(new_data[l//2-1])
        median = (m1 + m2)/2
    else:
        median = float(new_data[l//2])

    print(median)

def Mode():
    data = Counter(new_data)
    ranges = {
        "50-60": 0,
        "60-70": 0,
        "70-80": 0
    }
    for height, occurence in data.items():
        if 50 < float(height) < 60:
            ranges["50-60"] += occurence
        elif 60 < float(height) < 70:
            ranges["60-70"] += occurence
        elif 70 < float(height) < 80:
            ranges["70-80"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in ranges.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    mode = int(mode)
    print(mode)

Mean()
Median()
Mode()
