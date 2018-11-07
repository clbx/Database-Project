from flask import Flask
from flask import render_template
from flask import request
import mysql.connector

class Status:
    error = ""


app = Flask(__name__)

status = Status()


mydb= mysql.connector.connect(
    host="database.clbx.io",
    user="test",
    passwd="12Password34",
    database="dev"
)



mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Courses")

data = mycursor.fetchall()

def queryGenerator(formData):

    if(formData.values()[0] != ""):
        query = formData.values()[0]
        return query

    # SELECT * FROM Courses WHERE CODE LIKE "%crs%"
    query = "SELECT * FROM Courses"
    if(getDeps(formData.values()[1]) != "null"):
        query += " WHERE CODE LIKE \"%" + getDeps(formData.values()[1]) + "%\""

    return query


@app.route('/')
def index():
    return render_template('index.html',data=data, status=status)


@app.route('/handle_data',methods=['POST'])
def handle_data():

    getdata = request.form
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



def getDeps(department):
    if(department == "all"):
        return "null"
    elif(department == "biology"):
        return "BIO"
    elif(department == "business"):
        return "BA"
    else:
        return "null"
