import pandas as pd
from config.sql_connection import engine

def get_everything ():
    query = "SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (one_table):
    query = f"SELECT * FROM {one_table} limit 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_emp (emp_no, birth_date, first_name, last_name, gender, hire_date):
    query = f""" insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) values 
    ("{emp_no}","{birth_date}","{first_name}","{last_name}",
    "{gender}","{hire_date}")"""

    engine.execute(query)