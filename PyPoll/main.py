#final
import os
import csv

csvpath = os.path.join('..', '..', '..', '08-01-2017-NB-Class-Repository-DATA', '02-HomeWork', '03-Python', 'Instructions', 'PyPoll', 'raw_data', 'election_data_2.csv')

votes = []
counter = 0
candidates = []
winner = 0
ballots = 0

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        candidate = row[2]
        votes.append(row[2])
        counter = counter + 1
        if candidate not in candidates:
            candidates.append(row[2])

#export to text file
output_path = os.path.join('output.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline= '') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------------------\n")
    txtfile.write("Total Votes: " + str(counter) + "\n")
    txtfile.write("-------------------------------------\n")
    for item in candidates:
        txtfile.write(item + ": " + str(round((votes.count(item)/counter)*100, 2)) + "% (" + str(votes.count(item)) + ")\n")
        if votes.count(item) > ballots:
            ballots = votes.count(item)
            winner = item
    txtfile.write("-------------------------------------\n")
    txtfile.write("Winner: " + winner + "\n")

#print to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())

