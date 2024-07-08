import csv

with open("Test_Data.csv") as csvfile:
    reader = csv.reader(csvfile)
    for column in reader:
        print(column[0], column[1], sep=":")
