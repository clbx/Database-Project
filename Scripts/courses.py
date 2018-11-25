import csv

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

#OUTPUT
# 0 - ID (Primary key for table)
# 1 - Course Name (AC 101)
# 2 - Course Extra (BU)
# 3 - Credits (4)
# 4 - idDept (2)


newdata = []

# ID
newdata.append(0)

# Course Name
temp = data[1][1]
temp = temp.partition('-')[0][:-1]
newdata.append(temp)

#Course Extra
temp = data[1][1]
temp = temp.partition('-')[2][:-1]
newdata.append(temp)

#Credits
newdata.append(data[1][7])

#ID Department
