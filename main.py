from flask import Flask, Request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
#import pscyopg2
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def sql_query():
    conn = pscyopg2.connect(
        database="databasename", user="databaseusername", host='localhost', port="1234"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Query to pull the image of Our Lord Toad from the database""")
    return cursor.execute


@app.route('/', methods=['POST'])
def update_database():
    conn = pscyopg2.connect(
        database="databasename", user="databaseusername", host='localhost', port="1234"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Query to update a record of the image of Our Lord Toad in the database""")


@app.route('/', methods=['PUT'])
def create_new_entry():
    conn = pscyopg2.connect(
        database="databasename", user="databaseusername", host='localhost', port="1234"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Query to create a new record of the image of Our Lord Toad in the database""")


app.run(debug=True)
