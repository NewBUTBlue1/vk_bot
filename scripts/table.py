import csv

data = []
with open('city.csv', encoding="windows-1251") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for x in reader:
        data.append(x["name"])