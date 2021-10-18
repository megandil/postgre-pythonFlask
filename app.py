#app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html") 
@app.route('/login',methods=['POST'])
def login():
    from flask import request
    user1=request.form.get("usuario")
    passwd=request.form.get("contraseña")
    base=request.form.get("bbdd")
    conn = psycopg2.connect(dbname=base, user=user1, password=passwd, host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT id FROM coches;")
    coches = cur.fetchall()
    ids=[]
    for coche in coches:
        ids.append(coche[0])
    return render_template("login.html",ids=ids)
