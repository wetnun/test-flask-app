import os
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app_path = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(app_path, 'template')

app = Flask(__name__, template_folder=template_path)

app.config['MYSQL_USER'] = 'devuser'
app.config['MYSQL_PASSWORD'] = 'FluffyBunny'
app.config['MYSQL_DB'] = 'devdb'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def hello():
    cur = mysql.connection.cursor()
    cur.execute('''select message from testing order by rand() limit 1''')
    rv = cur.fetchall()
    return render_template('index.html', message=rv[0]['message'])

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

