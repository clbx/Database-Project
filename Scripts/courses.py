import csv


class Course:
    courseID = ""
    courseName = ""
    courseExt = ""
    credits = 0
    dpt = 0
    def __init__(self,courseID,courseName,courseExt,credits,dpt):
        self.courseID = courseID
        self.courseName = courseName
        self.courseExt = courseExt
        self.credits = credits
        self.dpt = dpt

data = []

# Get all of our data in
with open('ScrapedCourses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

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

#OUTPUT
# 0 - ID (Primary key for table)
# 1 - Course Name (AC 101)
# 2 - Course Extra (BU)
# 3 - Credits (4)
# 4 - idDept (2)


newdata = []

for i in range(len(data)):

    courseName = data[i][2]

    # Course Name
    temp = data[i][1]
    courseID = temp.partition('-')[0][:-1]

    #Course Extra
    temp = data[i][1]
    courseExtra = temp.partition('-')[2][:-1]

    #Credits
    credits = data[i][7]

    #ID Department
    temp = data[i][1]
    dpt = temp.partition('-')[0][:-1]
    if "BIO" in dpt:
        idd = 1
    elif "AC" in dpt or "BA" in dpt or "EC" in dpt or "FBE" in dpt or "FIN" in dpt or "FPA" in dpt:
        idd = 2
    elif "CH" in dpt:
        idd = 3
    elif "CSC" in dpt:
        idd = 4
    elif "COM" in dpt:
        idd = 5
    elif "CS" in dpt or "DS" in dpt:
        idd = 6
    elif "CW" in dpt:
        idd = 7
    elif "DAT" in dpt:
        idd = 8
    elif "ED" in dpt or "MCI" in dpt or "MSE" in dpt or "SED" in dpt:
        idd = 9
    elif "EGR" in dpt or "PHY" in dpt or "ES" in dpt:
        idd = 10
    elif "EN" in dpt or "HEN" in dpt or "LAT" in dpt:
        idd = 11
    elif "ART" in dpt or "MU" in dpt or "TH" in dpt or "DA" in dpt:
        idd = 12
    elif "PE" in dpt:
        idd = 13
    elif "HI" in dpt or "PHS" in dpt:
        idd = 14
    elif "IC" in dpt:
        idd = 15
    elif "MA" in dpt:
        idd = 16
    elif "ESL" in dpt or "FR" in dpt or "GER" in dpt or "JA" in dpt or "SP" in dpt:
        idd = 17
    elif "OT" in dpt or "ASL" in dpt:
        idd = 18
    elif "PCS" in dpt:
        idd = 19
    elif "PH" in dpt or "PP" in dpt or "PS" in dpt:
        idd = 20
    elif "PSY" in dpt or "HPC" in dpt:
        idd = 21
    elif "REL" in dpt:
        idd = 22
    elif "SW" in dpt:
        idd = 23
    elif "AN" in dpt or "SO" in dpt:
        idd = 24
    elif "WGS" in dpt:
        idd = 25
    elif "ILS" in dpt:
        idd = 26
    elif "INT" in dpt:
        idd = 27
    else:
        idd = 0

    course = Course(courseID,courseName,courseExtra,credits,idd)

    flag = True

    for row in newdata:
        if row.courseName == course.courseName:
            flag = False

    if flag is True:
        newdata.append(course);

with open('courses.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)

    for i in range(len(newdata)):
        w.writerow([newdata[i].courseID,newdata[i].courseName,newdata[i].courseExt,newdata[i].credits,newdata[i].dpt])
