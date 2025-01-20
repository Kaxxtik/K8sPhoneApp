# Import Flask modules
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import os

# Create an object named app
app = Flask(__name__)

# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')

# Initialize MySQL
mysql = MySQL()
mysql.init_app(app) 
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Function to find persons in the database
def find_persons(keyword):
    query = """
    SELECT * FROM phonebook WHERE name LIKE %s;
    """
    cursor.execute(query, ('%' + keyword.strip().lower() + '%',))
    result = cursor.fetchall()
    persons = [{'id': row[0], 'name': row[1].strip().title(), 'number': row[2]} for row in result]
    
    if len(persons) == 0:
        persons = [{'name': 'No Result', 'number': 'No Result'}]
    
    return persons

# Function to handle the search request
@app.route('/', methods=['GET', 'POST'])
def find_records():
    if request.method == 'POST':
        keyword = request.form['username']
        persons = find_persons(keyword)
        return render_template('index.html', persons=persons, keyword=keyword, show_result=True, developer_name='Kartik')
    else:
        return render_template('index.html', show_result=False, developer_name='Kartik')

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
