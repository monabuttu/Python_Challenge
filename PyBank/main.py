# import csv module
import csv

# import os module
import os

# Path to collect data from the Resources folder

cwd = os.getcwd()
print(cwd)

budget_csv = os.path.join(cwd,"..","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Homework","Instructions","PyBank","Resources","budget_data.csv")

# set starting month counter
months = 0

# set starting profit/loss counter
nettotal = 0

# create list for all proft/losses values

profitlosses = []

# set counter for change value

profitlosseschange = []

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
    
    for index, item in enumerate(profitlosses[0:-1]):
        profitlosseschange.append(int(profitlosses[index+1]) - int(profitlosses[index]))
    
    print(profitlosseschange)
    
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
print(f'Average Change: ${"{0:.2f}".format(Avchange)}')
print(f'Greatest Increase in Profits: ($)')
print(f'Greatest decrease in Profits: ($)')
print("------------------------------------------------------------------------")

# grab the location that you are writing to

outputpath = os.path.join(cwd,"..","bank_data.txt")

# Write data to text file

with open(outputpath, "w",newline="") as textfile:
    textfile.write("------------------------------------------------------------------------\n")
    textfile.write("Financial Anaylsis\n")
    textfile.write("------------------------------------------------------------------------\n")
    textfile.write(f'Total Months: {months}\n')
    textfile.write(f'Net Total: ${nettotal}\n')
    textfile.write(f'Average Change: ${"{0:.2f}".format(Avchange)}\n')
    textfile.write(f'Greatest Increase in Profits: ($)\n')
    textfile.write(f'Greatest decrease in Profits: ($)\n')
    textfile.write("------------------------------------------------------------------------\n")
