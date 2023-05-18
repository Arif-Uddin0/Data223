import csv

#Read

with open('new_user_data.csv', 'r') as usr_data:
    reader = csv.reader(usr_data)
    for row in reader:
        print(row)

with open('user_details.csv', 'r') as usr_details:
    reader1 = csv.DictReader(usr_details)
    rows = list(reader1)
    print(rows)

with open("hamlet.txt", "r") as hamlet:
    contents = hamlet.read()
    print(contents)

file = open("ETLvsELT.txt", 'r')
text = file.read()
print(text)
file.close()