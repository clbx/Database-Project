import csv

data = []

class room:
    roomNumber = ""
    buildingCode = 0
    def __init__(self,roomNumber,buildingCode):
        self.roomNumber = roomNumber
        self.buildingCode = buildingCode

# Get all of our data in
with open('ScrapedCourses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)



newdata = []


for i in range(len(data)):

    #print(data[i][6])

    #idBuilding + Room

    temp = data[i][6]
    temp2 = temp.partition(" ")[2]
    temp3 = temp2.partition(" ")[2]
    #building
    buildingCode = temp3.partition(" ")[0]
    #room
    roomNumber = temp3.partition(" ")[2]

    buildingID = 0
    if(buildingCode == "ONLINE"):
        buildingID = 1
    elif(buildingCode == "E"):
        buildingID = 2
    elif(buildingCode == "H"):
        buildingID = 3
    elif(buildingCode == "L"):
        buildingID = 4
    elif(buildingCode == "MU"):
        buildingID = 5
    elif(buildingCode == "N"):
        buildingID = 6
    elif(buildingCode == "BSC"):
        buildingID = 7
    elif(buildingCode == "R"):
        buildingID = 8
    elif(buildingCode == "ST"):
        buildingID = 9
    elif(buildingCode == "TH"):
        buildingID = 10
    elif(buildingCode == "W"):
        buildingID = 11
    elif(buildingCode == "YC"):
        buildingID = 12
    elif(buildingCode == "Z"):
        buildingID = 13
    else:
        buildingID = 0

    if(roomNumber != 0 and buildingID != 0):

        flag = True

        newroom = room(roomNumber,buildingID)
        #print(str(newroom.id) + " " + newroom.roomNumber + " " + str(newroom.buildingCode))


        for row in newdata:
            if row.roomNumber == newroom.roomNumber and row.buildingCode == newroom.buildingCode:
                flag = False
        if flag is True:
            newdata.append(newroom)


with open('file.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)

    for i in range(len(newdata)):
        w.writerow([i,newdata[i].roomNumber,newdata[i].buildingCode])


    #print("INSERT INTO `dev`.`room` (`idRoom`, `roomNumber`, `building`) VALUES ('"+ str(row.id)+"', '"+row.roomNumber +"', '"+str(row.buildingCode)+"');")
