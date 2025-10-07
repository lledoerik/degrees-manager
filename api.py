from flask import Flask,request,jsonify
from dao_degree import update_degree, delete_degree, insert_degree, show_degrees, dao_degree
from db_connection import db_connection


app = Flask(__name__)
dao = dao_degree()

@app.route("/login", methods=["GET"])
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    con = db_connection(user,password)
    conn = con.connection_bd()
    dao.login(conn)
    if conn.is_connected():
        return jsonify({"login": True})
    else:
        return jsonify({"login": False})


@app.route("/insert")
def insert_degree_api():
    degree = request.args.get("degree")
    user = request.args.get("user")
    password = request.args.get("password")
    result = insert_degree(degree, user, password)
    return jsonify({"status": "success", "message": "Degree inserted"})


@app.route("/show", methods=["GET"])
def show_degrees_api():
    table = request.args.get("table")
    user = request.args.get("user")
    password = request.args.get("password")
    array = show_degrees(table, user, password)
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
