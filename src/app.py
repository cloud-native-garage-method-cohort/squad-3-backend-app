import os
import psycopg2
import json
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_USER = os.environ["DATABASE_USER"]


@app.route("/")
def index():
    msg = {"msg": "Hello from the backend app"}
    return jsonify(msg)


@app.route("/api/employees", methods=["GET", "POST"])
def employeeEP():
    msg = ""
    if request.method == "GET":
        """get all employees"""
        conn = None
        try:
            conn = psycopg2.connect(
                host=DATABASE_URL,
                database=DATABASE_NAME,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                port=DATABASE_PORT,
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empl.employee")
            allEmployees = cursor.fetchall()
            employeeArray = []
            for row in allEmployees:
                employeeArray.append({"firstName": row[1], "lastName": row[2], "email": row[3]})

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching all employees from the database", error)

        finally:
            if conn:
                cursor.close()
                conn.close()

        msg = {"employees": employeeArray}

    if request.method == "POST":
        """create a new employee"""
        data = request.get_json()
        conn = None
        try:
            conn = psycopg2.connect(
                host=DATABASE_URL,
                database=DATABASE_NAME,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                port=DATABASE_PORT,
            )

            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO empl.employee (firstname, lastname, email) VALUES(%s, %s, %s)",
                (data["firstName"], data["lastName"], data["email"]),
            )
            conn.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while inserting an employee into the database", error)

        finally:
            if conn:
                cursor.close()
                conn.close()

        msg = {"msg": "OK"}

    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9010)
