from flask import Flask
from flask import render_template
from flask import request
import mysql.connector


app = Flask(__name__)


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

    # SELECT * FROM Courses WHERE CODE LIKE "%crs%"
    query = "SELECT * FROM Courses"
    if(getDeps(formData.values()[0]) != "null"):
        query += " WHERE CODE LIKE \"%" + getDeps(formData.values()[0]) + "%\""

    return query


@app.route('/')
def index():
    return render_template('index.html',data=data)


@app.route('/handle_data',methods=['POST'])
def handle_data():

    getdata = request.form
    query = queryGenerator(getdata)

    print(query)

    mycursor.execute(query)
    data = mycursor.fetchall()
    print(getdata)

    return render_template('index.html',data=data)



def getDeps(department):
    if(department == "biology"):
        return "BIO"
    elif(department == "business"):
        return "BA"
    else:
        return "null"
