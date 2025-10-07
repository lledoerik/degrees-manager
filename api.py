from flask import Flask,request,jsonify
from dao_degree import dao_degree
from db_connection import db_connection


app = Flask(__name__)
dao = dao_degree()

@app.route("/login", methods=["GET"])
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    con = db_connection(user, password)
    conn = con.connection_bd()
    
    success = False
    if conn and conn.is_connected():
        success = dao.login(conn)

    return jsonify({"login": success})


@app.route("/insert")
def insert_degree_api():
    degree = request.args.get("degree")
    user = request.args.get("user")
    password = request.args.get("password")
    result = dao.insert_degree(degree, user, password)
    return jsonify({"status": "success", "message": "Degree inserted"})


@app.route("/show", methods=["GET"])
def show_degrees_api():
    table = request.args.get("table")
    array = dao.show_degrees(table)
    return jsonify([d.to_dict() for d in array])


@app.route("/update")
def update_degree_api():
    table = request.args.get("table")
    user = request.args.get("user")
    password = request.args.get("password")
    result = update_degree(table, user, password)
    return jsonify({"status": "success", "message": "Degree updated"})


@app.route("/delete")
def delete_degree_api():
    table = request.args.get("table")
    user = request.args.get("user")
    password = request.args.get("password")
    result = delete_degree(table, user, password)
    return jsonify({"status": "success", "message": "Degree deleted"})


app.run()
