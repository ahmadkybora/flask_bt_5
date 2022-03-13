import pymysql
from flask import jsonify, redirect
from Models import Connection
from Connection import mysql
from flask_sqlalchemy import SQLAlchemy

class User:
    
    conn = None
    cursor = None

    def getAllUser(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()
