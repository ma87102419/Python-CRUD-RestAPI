from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="employeedb",
        user="postgres",
        password="12345",
        port="5432"
    )
    return conn


@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    return jsonify(rows)


@app.route('/employees', methods=['POST'])
def create_employee():
    conn = get_db_connection()
    cur = conn.cursor()
    data = request.get_json()
    name = data['name']
    age = data['age']
    education = data['education']
    experience = data['experience']
    profile = data['profile']
    department = data['department']
    salary = data['department']
    cur.execute("INSERT INTO employee (name, age, education, experience, profile, department, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name, age, education, experience, profile, department, salary))
    conn.commit()
    return jsonify({'message': 'Employee created successfully'})


@app.route('/employees/<string:name>', methods=['PUT'])
def update_employee(name):
    conn = get_db_connection()
    cur = conn.cursor()
    data = request.get_json()
    age = data['age']
    education = data['education']
    experience = data['experience']
    profile = data['profile']
    department = data['department']
    salary = data['salary']
    cur.execute("UPDATE employee SET age=%s, education=%s, experience=%s, profile=%s, department=%s, salary=%s WHERE name=%s",
                (age, education, experience, profile, department, salary, name))
    conn.commit()
    return jsonify({'message': 'Employee updated successfully'})


@app.route('/employees/<string:name>', methods=['DELETE'])
def delete_employee(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employee WHERE name=%s", (name,))
    conn.commit()
    return jsonify({'message': 'Employee deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
