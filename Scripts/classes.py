import csv
import re

# Python script to read course data and put it into sql queries

class cls:
    id = 0
    courseID = 0
    facultyID = 0
    status = ""
    seatsOpen = 0
    seatsTotal = 0
    days = ""
    time = ""
    roomID = ""
    def printOut(self):
        print(self.id + " " + self.courseID + " " + self.facultyID + " " + self.status + " " + self.seatsOpen + " " + self.seatsTotal + " " + self.days + " " + self.time + " " + self.roomID)




faculty = []
room = []
building = []
data = []
courses = []

# Get all of our data in
with open('ScrapedCourses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

with open('faculty.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        faculty.append(row)

with open('building.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        building.append(row)

with open('rooms.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        room.append(row)

with open('courses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        courses.append(row)

# Now to parse the raw csv





# INPUT
# 0 - Course ID [36390]
# 1 - Course Code, also contains Department [AC 101 - -BU - - A]
# 2 - Name of Class [INTRODUCTION TO ACCOUNTING]
# 3 - Instructor [Miller, Jared]
# 4 - Status [Open]
# 5 - Seats Open/Total [35/35]
# 6 - Time offered & Room [MWF (12:30pm-1:40pm) H 215]
# 7 - Credits

# OUTPUT
# 0 - ID (PK For Table)
# 1 - Course ID (FK from Courses)
# 2 - Faculty ID (FK from Faculty)
# 3 - status Class (Open/Closed)
# 4 - seatsOpen (Open Seats)
# 5 - seatstTotal (Total Seats)
# 6 - timeDays (Days Class is on)
# 7 - timeHours (Time class is)
# 8 - idRoom (FK from Rooms)

newdata = []


for i in range(len(data)-1):


    newclass = cls()

    #idClass
    newclass.id = data[i][0]

    #codeClass
    temp = data[i][1]
    courseID = 0
    code = temp.partition('-')[0][:-1]

    for i in range(len(data)):
        if(code == courses[i][1]):
            courseID = courses[i][0]
            break
    newclass.courseID = courseID


    #idFaculty


    facultyM = data[i][3]
    facultyID = 0
    lname = facultyM.partition(',')[0]
    fname = facultyM.partition(',')[2][1:]


    for i in range(len(faculty)):
        if(faculty[i][1] == fname and faculty[i][2] == lname):
            facultyID = faculty[i][0]
            break

    newclass.facultyID = facultyID



    #statusClass
    newclass.status = data[i][4]

    #Seats Open / Seats Closed
    temp = data[i][5]

    newclass.seatsOpen = temp.partition('/')[0]
    newclass.seatsTotal = temp.partition('/')[2]

    #timeDays
    temp = data[i][6]
    newclass.days = temp.partition(" ")[0]

    #timeHours
    temp2 = temp.partition("(")[2]
    temp3 = temp2.partition(")")[0]
    newclass.time = temp3


    #idBuilding + Room
    temp = data[i][6]
    temp2 = temp.partition(" ")[2]
    temp3 = temp2.partition(" ")[2]
    buildingN = temp3.partition(" ")[0]
    roomN = temp3.partition(" ")[2]
    buildingCode = ""

    for i in range(len(building)):
        if(buildingN == building[i][2]):
            buildingCode = courses[i][0]
            break
    for i in range(len(room)):
        if(buildingCode == room[i][2] and roomN == room[i][1]):
            roomID = room[i][0]

    newclass.roomID = roomID

    newdata.append(newclass)


#for i in range(len(data)):
newdata[2].printOut()

with open('classes.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)

    for i in range(len(newdata)):
        w.writerow([newdata[i].id,newdata[i].courseID,newdata[i].facultyID,newdata[i].status,newdata[i].seatsOpen,newdata[i].seatsTotal,newdata[i].days,newdata[i].time,newdata[i].roomID])
