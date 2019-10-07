# import csv module
import csv

# import os module
import os

# Path to collect data from the Resources folder

cwd = os.getcwd()

budget_csv = os.path.join('C:\\Users\\HP Book Pro\\Documents\\GitHub\\UT-TOR-DATA-PT-09-2019-U-C\\Unit 3 - Python\\Homework\\Instructions\\PyBank\\Resources',"budget_data.csv")

# set starting month counter
months = 0

# set starting profit/loss counter
nettotal = 0

# create list for all proft/losses values

profitlosses = []

# create average function

def averagechange(firstprice,secondprice):
    return (int(secondprice) - int(firstprice)) / months

# Read in the CSV file
with open(budget_csv, 'r', encoding="utf8") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # store header row/Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # count number of month are included in the data set
    for row in csvreader:
        months += 1
        nettotal += (int(row[1]))
        profitlosses.append(row[1])
        

# store first price

startprice = profitlosses[0]

# store second price

lastprice = profitlosses[-1]

# calculate average change

Avchange = averagechange(startprice,lastprice)

# Once the financial analysis is complete

print("------------------------------------------------------------------------")
print("Financial Anaylsis")
print("------------------------------------------------------------------------")
print(f'Total Months: {months}')
print(f'Net Total: ${nettotal}')
print(f'Average Change: {Avchange}')
print("Greatest Increase in Profits:")
print("Greatest decrease in Profits:")
print("------------------------------------------------------------------------")

# Export text file with the results