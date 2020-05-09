from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='prasant'
app.config['MYSQL_PASSWORD']='Janwar@1'
app.config['MYSQL_DB']='first_db'

mysql = MySQL(app)

@app.route('/', methods = ['GET','POST'])
def hello():
    if request.method=='POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
