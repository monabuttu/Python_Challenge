# import csv module
import csv

# import os module
import os

# Path to collect data from the Resources folder

cwd = os.getcwd()

election_csv = os.path.join(cwd,"..","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Homework","Instructions","PyPoll","Resources","election_data.csv")

# set starting count for total votes
totalvotes = 0 

# dictionary to start counter and store winning votes for each candidate

candidatevotes = {"Correy":0,"Li":0,"O'Tooley":0,"Khan":0}

# create function to calculate percentage won

def percent_won(individualvotes):
    return (individualvotes / totalvotes) * 100

# Read in the CSV file
with open(election_csv, 'r', encoding="utf8") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # store header row/Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        totalvotes += 1
        if row[2] == "Khan":
            candidatevotes["Khan"] += 1
        elif row[2] == "Correy":
            candidatevotes["Correy"] += 1
        elif row[2] == "Li":
            candidatevotes["Li"] += 1
        elif row[2] == "O'Tooley":
            candidatevotes["O'Tooley"] += 1


# calculate percent won per candidate

KhanWinPercent = percent_won(candidatevotes["Khan"])
CorreyWinPercent = percent_won(candidatevotes["Correy"])
OTooleyWinPercent = percent_won(candidatevotes["O'Tooley"])
LiWinPercent = percent_won(candidatevotes["Li"])

# put values in a list
winninglist = [KhanWinPercent,CorreyWinPercent,OTooleyWinPercent,LiWinPercent]

# find winner from list using max function
winner = max(winninglist)

# Once the election analysis is complete
print("_____________________________________________")
print("Election Results")
print("---------------------------------------------")
print(f'Total Votes: {totalvotes}')
print("---------------------------------------------")

# print number of winning votes for each candidate

print(f'Khan: {"{0:.3f}".format(KhanWinPercent)}  ({candidatevotes["Khan"]} votes)')
print(f'Correy: {"{0:.3f}".format(CorreyWinPercent)} ({candidatevotes["Correy"]} votes)')
print("O'Tooley: " + str("{0:.3f}".format(OTooleyWinPercent)) + "(" + str(candidatevotes["O'Tooley"]) + " votes" + ")")
print(f'Li: {"{0:.3f}".format(LiWinPercent)} ({candidatevotes["Li"]} votes)')
print("---------------------------------------------")

# print winner
if winner == KhanWinPercent:
    print(f'Winner: Khan')
elif winner == CorreyWinPercent:
    print(f'Winner: Correy')
elif winner == OTooleyWinPercent:
    print(f"Winner: O'Tooley")
elif winner == LiWinPercent:
    print(f'Winner: Li')

# grab the location that you are writing to

outputpath = os.path.join(cwd,"..","election_data.txt")

# Write data to text file

with open(outputpath, "w",newline="") as textfile:
    textfile.write(f'Total Votes: {totalvotes}\n')
    textfile.write(f'Khan: {"{0:.3f}".format(KhanWinPercent)}  ({candidatevotes["Khan"]} votes)\n')
    textfile.write(f'Correy: {"{0:.3f}".format(CorreyWinPercent)} ({candidatevotes["Correy"]} votes)\n')
    textfile.write("O'Tooley: " + str("{0:.3f}".format(OTooleyWinPercent)) + "(" + str(candidatevotes["O'Tooley"]) + " votes" + ")\n")
    textfile.write(f'Li: {"{0:.3f}".format(LiWinPercent)} ({candidatevotes["Li"]} votes)\n')
    if winner == KhanWinPercent:
        textfile.write(f'Winner: Khan')
    elif winner == CorreyWinPercent:
        textfile.write(f'Winner: Correy')
    elif winner == OTooleyWinPercent:
        textfile.write(f"Winner: O'Tooley")
    elif winner == LiWinPercent:
        textfile.write(f'Winner: Li')
