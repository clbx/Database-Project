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
    user="test",
    passwd="12Password34",
    database="dev"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Courses")

data = mycursor.fetchall()



@app.route('/')
def index():
    return render_template('index.html',data=data, status=status)


@app.route('/handle_data',methods=['POST'])
def handle_data():

    getdata = request.form
    del constraints [:]
    query = ""


    query = queryGenerator(getdata)

    print(query)
    try:
        mycursor.execute(query)
        data = mycursor.fetchall()
        status.error = ""
    except mysql.connector.Error as err:
        data = "";
        status.error = ("Error: {}".format(err))

    print(getdata)

    return render_template('index.html',data=data, status=status)

def queryGenerator(formData):

    if(formData.values()[0] != ""):
        query = formData.values()[0]
        return query

    # SELECT * FROM Courses WHERE CODE LIKE "%crs%"
    query = "SELECT * FROM Courses" + constraintGenerator(formData)

    return query

def constraintGenerator(formData):

    getDeps(formData.values()[1])
    getCore(formData.values()[2])

    print("Form val: ")
    for constraint in constraints:
        print("Key: "+ constraint.key+" Value "+constraint.value)

    queryConst = ""
    #Process constraints
    if(len(constraints) > 0):
        if(constraints[0].type == "LIKE"):
            queryConst += " WHERE " + constraints[0].key + " LIKE \"" + constraints[0].value + "\""
        #if(constraints[0].type == "GREATER"):

        #if(constraints[0].type == "LESS"):
    i = 1
    for constraint in constraints[1:]:
        if(constraints[i].type == "LIKE"):
            queryConst += " OR " + constraints[i].key + " LIKE \"" + constraints[i].value + "\""
        #if(constraints[0].type == "GREATER"):

        #if(constraints[0].type == "LESS"):

        i += 1

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
        constraints.append(Constraint("LIKE","CODE","%BIO%"))
    elif(department == "business"):
        constraints.append(Constraint("LIKE","CODE","%BA%"))
        constraints.append(Constraint("LIKE","CODE","%EC%"))
        constraints.append(Constraint("LIKE","CODE","%FBE%"))
        constraints.append(Constraint("LIKE","CODE","%FIN%"))
        constraints.append(Constraint("LIKE","CODE","%FPA%"))
    elif(department == "chemistry"):
        constraints.append(Constraint("LIKE","CODE","%CH %"))
    elif(department == "cognitive"):
        constraints.append(Constraint("LIKE","CODE","%CSC%"))
    elif(department == "communications"):
        constraints.append(Constraint("LIKE","CODE","%COM%"))
    elif(department == "compsci"):
        constraints.append(Constraint("LIKE","CODE","CS %"))
        constraints.append(Constraint("LIKE","CODE","%DS %"))
    elif(department == "writing"):
        constraints.append(Constraint("LIKE","CODE","%CW%"))
    elif(department == "data"):
        constraints.append(Constraint("LIKE","CODE","%DAT%"))
    elif(department == "education"):
        constraints.append(Constraint("LIKE","CODE","%ED%"))
        constraints.append(Constraint("LIKE","CODE","%MCI%"))
        constraints.append(Constraint("LIKE","CODE","%MSE%"))
        constraints.append(Constraint("LIKE","CODE","%SED%"))
    elif(department == "engineering"):
        constraints.append(Constraint("LIKE","CODE","%EGR%"))
        constraints.append(Constraint("LIKE","CODE","%PHY%"))
        constraints.append(Constraint("LIKE","CODE","%ES%"))
    elif(department == "english"):
        constraints.append(Constraint("LIKE","CODE","%EN%"))
        constraints.append(Constraint("LIKE","CODE","%HEN%"))
        constraints.append(Constraint("LIKE","CODE","%LAT%"))
    elif(department == "arts"):
        constraints.append(Constraint("LIKE","CODE","%ART%"))
        constraints.append(Constraint("LIKE","CODE","%MU%"))
        constraints.append(Constraint("LIKE","CODE","%TH%"))
        constraints.append(Constraint("LIKE","CODE","%DA%"))
    elif(department == "health"):
        constraints.append(Constraint("LIKE","CODE","%PE%"))
    elif(department == "history"):
        constraints.append(Constraint("LIKE","CODE","%HI%"))
        constraints.append(Constraint("LIKE","CODE","%PHS%"))
    elif(department == "is"):
        constraints.append(Constraint("LIKE","CODE","%IC%"))
    elif(department == "interfaith"):
        constraints.append(Constraint("LIKE","CODE","%ILS%"))
    elif(department == "international"):
        constraints.append(Constraint("LIKE","CODE","%INT%"))
    elif(department == "math"):
        constraints.append(Constraint("LIKE","CODE","%MA%"))
    elif(department == "lang"):
        constraints.append(Constraint("LIKE","CODE","%ESL%"))
        constraints.append(Constraint("LIKE","CODE","%FR%"))
        constraints.append(Constraint("LIKE","CODE","%GER%"))
        constraints.append(Constraint("LIKE","CODE","%JA%"))
        constraints.append(Constraint("LIKE","CODE","%SP%"))
    elif(department == "ot"):
        constraints.append(Constraint("LIKE","CODE","%OT%"))
        constraints.append(Constraint("LIKE","CODE","%ASL%"))
    elif(department == "peace"):
        constraints.append(Constraint("LIKE","CODE","%PCS%"))
    elif(department == "ppls"):
        constraints.append(Constraint("LIKE","CODE","%PH %"))
        constraints.append(Constraint("LIKE","CODE","%PP %"))
        constraints.append(Constraint("LIKE","CODE","%PS %"))
    elif(department == "psychology"):
        constraints.append(Constraint("LIKE","CODE","%PSY%"))
        constraints.append(Constraint("LIKE","CODE","%HPC%"))
    elif(department == "religious"):
        constraints.append(Constraint("LIKE","CODE","%REL%"))
    elif(department == "socialwork"):
        constraints.append(Constraint("LIKE","CODE","%SW%"))
    elif(department == "sociology"):
        constraints.append(Constraint("LIKE","CODE","%AN%"))
        constraints.append(Constraint("LIKE","CODE","%SO%"))
    elif(department == "gender"):
        constraints.append(Constraint("LIKE","CODE","%WGS%"))
    else:
        return
def getCore(core):
    if(core == "0IC"):
        constraints.append(Constraint("LIKE","CODE","%10IC%"))
    elif(core == "CE"):
        constraints.append(Constraint("LIKE","CODE","%3CE%"))
    elif(core == "HUM"):
        constraints.append(Constraint("LIKE","CODE","%9HUM%"))
    elif(core == "MA"):
        constraints.append(Constraint("LIKE","CODE","%8MA%"))
    elif(core == "NCH"):
        constraints.append(Constraint("LIKE","CODE","%5NCH%"))
    elif(core == "NPS"):
        constraints.append(Constraint("LIKE","CODE","%6NPS%"))
    elif(core == "PLE"):
        constraints.append(Constraint("LIKE","CODE","%1PLE%"))
    elif(core == "PLO"):
        constraints.append(Constraint("LIKE","CODE","%2PLO%"))
    elif(core == "SSC"):
        constraints.append(Constraint("LIKE","CODE","%7SSC%"))
    elif(core == "WCH"):
        constraints.append(Constraint("LIKE","CODE","%4WCH%"))
