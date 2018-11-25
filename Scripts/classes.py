import csv
import re

# Python script to read course data and put it into sql queries


data = []

# Get all of our data in
with open('ScrapedCourses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Now to parse the raw csv
print(data[1])




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

#idClass
newdata.append(data[1][0])

temp = data[1][1]
#codeClass
temp = temp.partition('-')[0][:-1]
newdata.append(temp)

#nameClass
newdata.append(data[1][2])

#idFaculty
newdata.append('123456')

#statusClass
temp = data[1][4]

print(temp)

if(temp == "Open"):
    newdata.append(1)
elif(temp == "Closed"):
    newdata.append(0)
elif(temp == "Cancelled"):
    newdata.append(2)

#Seats Open / Seats Closed
temp = data[1][5]

newdata.append(temp.partition('/')[0])
newdata.append(temp.partition('/')[2])

#timeDays
temp = data[1][6]
newdata.append(temp.partition(" ")[0])

#timeHours
temp2 = temp.partition("(")[2]
temp3 = temp2.partition(")")[0]
newdata.append(temp3)

#creditsClass
newdata.append(data[1][7])

#idBuilding + Room
temp = data[1][6]
temp2 = temp.partition(" ")[2]
temp3 = temp2.partition(" ")[2]
newdata.append(temp3.partition(" ")[0])
newdata.append(temp3.partition(" ")[2])










print(newdata)
#for i in range(len(data)):
