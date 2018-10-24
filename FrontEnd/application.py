from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'dev'
app.config['MYSQL_DATABASE_HOST'] = 'database.clbx.io'
mysql.init_app(app)


@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from Courses")
    data = cursor.fetchall()
    return render_template('index.html',data=data)
