#Import operating system and csv
import os
import csv

#Open and read csv 
budget_csv = os.path.join("budget_data.csv")
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    next(csvreader)

    #Lists to store data
    date = []

#Read through each row of csv
    for row in csvreader:

# Loop through column to add Voter IDs
        date.append(row[0])

#Calculate the total number of votes cast and print
total_months = len(date)
print(f'Total Months: {len(date)}')


