#final
import os
import csv

csvpath = os.path.join('..', '..', '..', '08-01-2017-NB-Class-Repository-DATA', '02-HomeWork', '03-Python', 'Instructions', 'PyBank', 'raw_data', 'budget_data_2.csv')

total_revenue = 0
total = 0
rev_change =[]
hiChange = 0
loChange = 0
hiDate = 0
loDate = 0
date = 0
counter = 0

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader)
    change = 0
    past_value = 0

    for row in csvreader:
        counter = counter + 1
        revenues = row[1]
        date = row[0]
        total_revenue += int(revenues)
    
        change = int(row[1]) - past_value

        if change > hiChange:
            hiChange = change
            hiDate = date

        if change < loChange:
            loChange = change
            loDate = date

        rev_change.append(change)
        
        past_value = int(row[1])

    #account for first month "change" which should not count
    rev_change.pop(0)
   
    for x in range(len(rev_change)):
        total += int(rev_change[x]) 
        aver = (int(total))/(int(len(rev_change)))

# Specify the file to write to
output_path = os.path.join('output.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline= '') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------------------\n") 
    txtfile.write("Total Months: " + str(counter) + "\n")
    txtfile.write("Total Revenue: $" + str(total_revenue)+ "\n")
    txtfile.write("Average Revenue Change: $" + str(round(aver, 2))+ "\n")
    txtfile.write("Greatest Increase in Revenue: " + str(hiDate) + " $" + str(hiChange)+ "\n")
    txtfile.write("Greatest Decrease in Revenue: " + str(loDate) + " $" + str(loChange)+ "\n")

#print to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())




        
        
     

