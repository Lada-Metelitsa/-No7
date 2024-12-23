from flask import Flask, render_template
import pandas as pd
import sqlite3

def create_database():
  data = pd.read_csv('data.csv')
  connection = sqlite3.connect('data.db')
  data.to_sql('data', connection, index=False, if_exists='replace')
  connection.close()

app = Flask(__name__)

create_database()


@app.route('/')
def index():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    connection.close()

    return render_template('code.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)