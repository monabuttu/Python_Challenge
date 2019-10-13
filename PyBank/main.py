# import csv module
import csv

# import os module
import os

# Path to collect data from the Resources folder

cwd = os.getcwd()
budget_csv = os.path.join(cwd,"..","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Homework","Instructions","PyBank","Resources","budget_data.csv")

# set starting month counter
months = 0

# set starting profit/loss counter
nettotal = 0

# create list for all proft/losses values

profitlosses = []

# create list for change values

profitlosseschange = []

# create date list

date = []

# create average function to calcluate average change in profit/losses

def averagechange(firstprice,secondprice):
    return (int(secondprice) - int(firstprice)) / months

# Read in the CSV file
with open(budget_csv, 'r', encoding="utf8") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # store header row/Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        # count number of month are included in the data set
        months += 1
        # add the profit/losses to nettotal
        nettotal += (int(row[1]))
        # add profit/loss value to profitlosses list
        profitlosses.append(row[1])
        # add date to date list
        date.append(row[0])
    
    # calculate change between each profit/loss value and store change in profitlosseschange list
    for index, item in enumerate(profitlosses[0:-1]):
        profitlosseschange.append(int(profitlosses[index+1]) - int(profitlosses[index]))
    
          
    # find greatest increase in profitlosseschange list
    maxchange = max(profitlosseschange)

    # find index position of greatest increase
    maxchangeindex = profitlosseschange.index(maxchange)

    # find greatest decrease in profitlosseschange list
    minchange = min(profitlosseschange)

    # find index position of greatest decrease
    maxchangeindex = profitlosseschange.index(minchange)
    
    
# store first price listed in data 

startprice = profitlosses[0]

# store last price listed in data

lastprice = profitlosses[-1]

# calculate average change over entire period

Avchange = averagechange(startprice,lastprice)

# Once the financial analysis is complete

print("------------------------------------------------------------------------")
print("Financial Anaylsis")
print("------------------------------------------------------------------------")
print(f'Total Months: {months}')
print(f'Net Total: ${nettotal}')
print(f'Average Change: ${"{0:.2f}".format(Avchange)}')
print(f'Greatest Increase in Profits: {(date[profitlosseschange.index(maxchange)+1])} (${maxchange})')
print(f'Greatest decrease in Profits: {(date[profitlosseschange.index(minchange)+1])} (${minchange})')
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
    textfile.write(f'Greatest Increase in Profits: {(date[profitlosseschange.index(maxchange)+1])} (${maxchange})\n')
    textfile.write(f'Greatest decrease in Profits: {(date[profitlosseschange.index(minchange)+1])} (${minchange})\n')
    textfile.write("------------------------------------------------------------------------\n")
