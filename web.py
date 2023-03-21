from flask import Flask
from flask_mysqldb import MySQL
from flask import render_template

app = Flask(__name__)

app.config['MYSQL_USER'] = 'rose'
app.config['MYSQL_PASSWORD'] = 'team0606'
app.config['MYSQL_HOST'] = '192.168.0.100'
app.config['MYSQL_DB'] = 'myDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
@app.route("/home")
def hello_world():
	return '<p>Welcome to our theater</p>'

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/data')
def CONNECT_DB():
    statement = mysql.connection.cursor()
    statement.execute('''SELECT * FROM movies''')
    Executed_DATA = statement.fetchall()
    print(Executed_DATA)
    return str(Executed_DATA[0])
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
