from flask import Flask, request, jsonify
import random
import tools.sql_queries as sql
import config.sql_connection as sqlconnect

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/random-number")
def random_int():
    return str(random.randint(0, 10))


@app.route("/everything-employees")
def example():
    return jsonify(sql.get_everything())

@app.route("/table/<one_table>")
def example2(one_table):
    return jsonify(sql.table_ten(one_table))


@app.route("/insert-into-employees", methods=["POST"])
def x ():
    emp_no=request.args["emp_no"]
    birth_date=request.args["birth_date"]
    first_name=request.args["first_name"]
    last_name=request.args["last_name"]
    gender=request.args["gender"]
    hire_date=request.args["hire_date"]

    sql.insert_emp(emp_no, birth_date, first_name, last_name, gender, hire_date)
    return "INSERTED"

if __name__ == "__main__":
    app.run (port=7071, debug=True)