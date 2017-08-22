import os
import csv

us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA', 'Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH',
    'New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI',
    'South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',}

csvpath = os.path.join('..', '..', '..', '08-01-2017-NB-Class-Repository-DATA', '02-HomeWork', '03-Python', 'Instructions', 'PyBoss', 'raw_data', 'employee_data2.csv')

empid = []

firstName = []
lastName = []

dates = []

SSN = []

newState = []

d = "/"

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        empid.append(row[0])

        newName = row[1].split(" ")
        firstName.append(newName[0])
        lastName.append(newName[1])

        newDate = row[2].split("-")
        fullDate = (newDate[1], newDate[2], newDate[0])
        dates.append(d.join(fullDate))

        newSSN = row[3].split("-")
        SSN.append("***-**-" + newSSN[2])

        newState.append(us_state_abbrev[row[4]])

employees = zip(empid, firstName, lastName, dates, SSN, newState)

output_path = os.path.join('output.csv')

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Employee ID', 'First Name', 'Last Name', 'Birth Date', 'SSN', 'State'])
    
    csvwriter.writerows(employees)