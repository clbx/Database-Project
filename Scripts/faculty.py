import csv

data = []

# Get all of our data in
with open('faculty.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)




newline = []


for i in range(0, len(data)):

    #FacultyID
    newline.append(0)


    #title / fname / minitial / lname
    name = data[i][1]
    spaces = name.count(" ")

    title = name.partition(" ")[0]
    newline.append(title)

    name = name.partition(" ")[2]

    fname = name.partition(" ")[0]
    newline.append(fname)
    name = name.partition(" ")[2]

    if(spaces == 3):
        minit = name.partition(" ")[0]
        lname = name.partition(" ")[2]
        newline.append(minit)
        newline.append(lname)

    elif(spaces == 2 or spaces == 4):
        lname = name

    else:
        print("ERROR on line " + str(i) + ". Found " + str(spaces) + " spaces")


    # ID Deparment
    newline.append(data[i][0])

    # Title
    newline.append(data[i][3])


    office = data[i][4]

    comma = office.count(",")

    if(comma > 0):
        building = office.partition(",")[0]
        newline.append(building)
        room = office.partition(",")[2][5:]
        newline.append(room)

    else:
        newline.append(office)


    newline.append(data[i][2])


print(newline)
