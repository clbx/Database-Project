from flask import Flask
from flask import render_template
from flask import request
import mysql.connector

class Status:
    error = ""


# Types: LIKE, GREATER, LESS
class Constraint:
    type = ""
    key = ""
    value = ""
    def __init__(self,type,key,value):
        self.type = type
        self.key = key
        self.value = value



app = Flask(__name__)

status = Status()
constraints = []

mydb= mysql.connector.connect(
    host="database.clbx.io",
    user="Present",
    passwd="12Password34",
    database="college"
)


mycursor = mydb.cursor()


bigquery = '''
SELECT
    Class.idClass as RefNo,
    Class.idCourse as CourseID,
    Course.courseName as \"Course Name\",
    concat(Faculty.fName,\" \",Faculty.lName) as Instructor,
    Class.statusClass as Status,
    concat(Class.seatsOpen,\"/\",Class.seatsTotal) as Seats,
    concat(Class.timeDays,\" \",Class.timeHours) as Times,
    concat(Building.abbreviation,\" \",Room.roomNumber) as Room,
    Course.credits as Credits
FROM college.Class, college.Course, college.Faculty, college.Room, college.Building
WHERE Class.idCourse = Course.idCourse
AND Class.idFaculty = Faculty.idFaculty
AND Class.idRoom = Room.idRoom
AND Room.building = Building.idBuilding
'''


mycursor.execute(bigquery)

data = mycursor.fetchall()

tableType = "main"

@app.route('/')
def index():
    return render_template('index.html',data=data, status=status,tableType=tableType)


@app.route('/handle_data',methods=['POST'])
def handle_data():

    tableType = "main"
    getdata = request.form
    del constraints [:]
    query = ""


    query, tableType = queryGenerator(getdata, tableType)

    print(query)
    try:
        mycursor.execute(query)
        data = mycursor.fetchall()
        status.error = ""
    except mysql.connector.Error as err:
        data = "";
        status.error = ("Error: {}".format(err))

    print(getdata)

    print(tableType)

    return render_template('index.html',data=data, status=status, tableType=tableType)

def queryGenerator(formData, tableType):


    if(formData.values()[0] != ""):
        query = formData.values()[0]
        tableType = "other"
        return query, tableType



    if(formData.values()[2] != ""):
        query = bigquery + "AND Course.courseName LIKE \"%" + formData.values()[2] + "%\""
        return query, tableType

    # SELECT * FROM Courses WHERE CODE LIKE "%crs%"
    query = bigquery + constraintGenerator(formData)

    return query, tableType

def constraintGenerator(formData):

    getDeps(formData.values()[1])
    getCore(formData.values()[3])

    print("Form val: ")
    for constraint in constraints:
        print("Key: "+ constraint.key+" Value "+constraint.value)

    queryConst = ""

    i = 0

    #Process constraints
    if(len(constraints) > 0):
        if(constraints[0].type == "LIKE"):
            queryConst += " AND( " + constraints[0].key + " LIKE \"" + constraints[0].value + "\""
        #if(constraints[0].type == "GREATER"):

        #if(constraints[0].type == "LESS"):
        i = 1
    for constraint in constraints[1:]:
        if(constraints[i].type == "LIKE"):
            queryConst += " OR " + constraints[i].key + " LIKE \"" + constraints[i].value + "\""
        #if(constraints[0].type == "GREATER"):

        #if(constraints[0].type == "LESS"):

        i += 1

    if( i > 0):
        queryConst += ")"

    return queryConst





'''
def oldgetDeps(department):
    if(department == "all"):
        return "null"
    elif(department == "biology"):
        return "WHERE CODE LIKE \"%BIO%\""
    elif(department == "business"):
        return "WHERE CODE LIKE \"%AC%\" OR CODE LIKE \"%BA%\" OR CODE LIKE \"%EC%\" OR CODE LIKE \"%FBE%\" OR CODE LIKE \"%FIN%\""
    elif(department == "chemistry"):
        return "WHERE CODE LIKE \"%CH %\""
    elif(department == "cognitive"):
        return "WHERE CODE LIKE \"%CSC%\""
    elif(department == "communications"):
        return "WHERE CODE LIKE \"%COM%\""
    elif(department == "compsci"):
        return "WHERE CODE LIKE \"CS %\" OR CODE LIKE \"%DS\""
    elif(department == "writing"):
        return "WHERE CODE LIKE \"%CW%\""
    elif(department == "data"):
        return "WHERE CODE LIKE \"%DAT%\""
    elif(department == "education"):
        return "WHERE CODE LIKE \"%ED%\" OR CODE LIKE \"%MCI%\" OR CODE LIKE \"%MSE%\" OR CODE LIKE \"%SED%\""
    elif(department == "engineering"):
        return "WHERE CODE LIKE \"%EGR%\" OR CODE LIKE \"%PHY%\""
    elif(department == "english"):
        return "WHERE CODE LIKE \"%EN%\" OR CODE LIKE \"%HEN%\" OR CODE LIKE \"%LAT%\""
    elif(department == "arts"):
        return "WHERE CODE LIKE \"%ART%\" OR CODE LIKE \"%MU%\" OR CODE LIKE \"%TH%\""
    elif(department == "health"):
        return "WHERE CODE LIKE \"%PE%\""
    elif(department == "history"):
        return "WHERE CODE LIKE \"%HI%\" OR CODE LIKE \"%PHS%\""
    elif(department == "is"):
        return "WHERE CODE LIKE \"%IC%\""
    elif(department == "interfaith"):
        return "WHERE CODE LIKE \"%ILS%\""
    elif(department == "international"):
        return "WHERE CODE LIKE \"%INT%\""
    elif(department == "math"):
        return "WHERE CODE LIKE \"%MA%\""
    elif(department == "lang"):
        return "WHERE CODE LIKE \"%ESL%\" OR CODE LIKE \"%FR%\" OR CODE LIKE \"%GER%\" OR CODE LIKE \"%JA%\" OR CODE LIKE \"%SP%\""
    elif(department == "ot"):
        return "WHERE CODE LIKE \"%OT%\""
    elif(department == "peace"):
        return "WHERE CODE LIKE \"%PCS%\""
    elif(department == "ppls"):
        return "WHERE CODE LIKE \"%PH %\" OR CODE LIKE \"%PP %\" OR CODE LIKE \"%PS %\""
    elif(department == "psychology"):
        return "WHERE CODE LIKE \"%PSY%\" OR CODE LIKE \"%HPC%\""
    elif(department == "religious"):
        return "WHERE CODE LIKE \"%REL%\""
    elif(department == "socialwork"):
        return "WHERE CODE LIKE \"%SW%\""
    elif(department == "sociology"):
        return "WHERE CODE LIKE \"%AN%\" OR CODE LIKE \"%SO%\""
    elif(department == "gender"):
        return "WHERE CODE LIKE \"%WGS%\""
    else:
        return "null"
'''

#TODO: Fix this monstrosity
def getDeps(department):
    if(department == "all"):
        return
    elif(department == "biology"):
        constraints.append(Constraint("LIKE","Course.idCourse","%BIO%"))
    elif(department == "business"):
        constraints.append(Constraint("LIKE","Course.idCourse","%BA%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%EC%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%FBE%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%FIN%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%FPA%"))
    elif(department == "chemistry"):
        constraints.append(Constraint("LIKE","Course.idCourse","%CH %"))
    elif(department == "cognitive"):
        constraints.append(Constraint("LIKE","Course.idCourse","%CSC%"))
    elif(department == "communications"):
        constraints.append(Constraint("LIKE","Course.idCourse","%COM%"))
    elif(department == "compsci"):
        constraints.append(Constraint("LIKE","Course.idCourse","CS %"))
        constraints.append(Constraint("LIKE","Course.idCourse","%DS %"))
    elif(department == "writing"):
        constraints.append(Constraint("LIKE","Course.idCourse","%CW%"))
    elif(department == "data"):
        constraints.append(Constraint("LIKE","Course.idCourse","%DAT%"))
    elif(department == "education"):
        constraints.append(Constraint("LIKE","Course.idCourse","%ED%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%MCI%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%MSE%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%SED%"))
    elif(department == "engineering"):
        constraints.append(Constraint("LIKE","Course.idCourse","%EGR%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%PHY%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%ES%"))
    elif(department == "english"):
        constraints.append(Constraint("LIKE","Course.idCourse","%EN%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%HEN%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%LAT%"))
    elif(department == "arts"):
        constraints.append(Constraint("LIKE","Course.idCourse","%ART%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%MU%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%TH%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%DA%"))
    elif(department == "health"):
        constraints.append(Constraint("LIKE","Course.idCourse","%PE%"))
    elif(department == "history"):
        constraints.append(Constraint("LIKE","Course.idCourse","%HI%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%PHS%"))
    elif(department == "is"):
        constraints.append(Constraint("LIKE","Course.idCourse","%IC%"))
    elif(department == "interfaith"):
        constraints.append(Constraint("LIKE","Course.idCourse","%ILS%"))
    elif(department == "international"):
        constraints.append(Constraint("LIKE","Course.idCourse","%INT%"))
    elif(department == "math"):
        constraints.append(Constraint("LIKE","Course.idCourse","%MA%"))
    elif(department == "lang"):
        constraints.append(Constraint("LIKE","Course.idCourse","%ESL%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%FR%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%GER%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%JA%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%SP%"))
    elif(department == "ot"):
        constraints.append(Constraint("LIKE","Course.idCourse","%OT%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%ASL%"))
    elif(department == "peace"):
        constraints.append(Constraint("LIKE","Course.idCourse","%PCS%"))
    elif(department == "ppls"):
        constraints.append(Constraint("LIKE","Course.idCourse","%PH %"))
        constraints.append(Constraint("LIKE","Course.idCourse","%PP %"))
        constraints.append(Constraint("LIKE","Course.idCourse","%PS %"))
    elif(department == "psychology"):
        constraints.append(Constraint("LIKE","Course.idCourse","%PSY%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%HPC%"))
    elif(department == "religious"):
        constraints.append(Constraint("LIKE","Course.idCourse","%REL%"))
    elif(department == "socialwork"):
        constraints.append(Constraint("LIKE","Course.idCourse","%SW%"))
    elif(department == "sociology"):
        constraints.append(Constraint("LIKE","Course.idCourse","%AN%"))
        constraints.append(Constraint("LIKE","Course.idCourse","%SO%"))
    elif(department == "gender"):
        constraints.append(Constraint("LIKE","Course.idCourse","%WGS%"))
    else:
        return
def getCore(core):
    if(core == "0IC"):
        constraints.append(Constraint("LIKE","Course.courseExt","%10IC%"))
    elif(core == "CE"):
        constraints.append(Constraint("LIKE","Course.courseExt","%3CE%"))
    elif(core == "HUM"):
        constraints.append(Constraint("LIKE","Course.courseExt","%9HUM%"))
    elif(core == "MA"):
        constraints.append(Constraint("LIKE","Course.courseExt","%8MA%"))
    elif(core == "NCH"):
        constraints.append(Constraint("LIKE","Course.courseExt","%5NCH%"))
    elif(core == "NPS"):
        constraints.append(Constraint("LIKE","Course.courseExt","%6NPS%"))
    elif(core == "PLE"):
        constraints.append(Constraint("LIKE","Course.courseExt","%1PLE%"))
    elif(core == "PLO"):
        constraints.append(Constraint("LIKE","Course.courseExt","%2PLO%"))
    elif(core == "SSC"):
        constraints.append(Constraint("LIKE","Course.courseExt","%7SSC%"))
    elif(core == "WCH"):
        constraints.append(Constraint("LIKE","Course.courseExt","%4WCH%"))
