from flask import Flask,request,jsonify
from dao_degree import update_degree, delete_degree, insert_degree, show_degrees

app = Flask(__name__)


@app.route("/insert")
def insert_degree_api():
    return insert_degree()



@app.route("/show", methods=["GET"])
def show_degrees_api():
    table = request.args.get("table")
    user = request.args.get("user")
    password = request.args.get("password")
    array = show_degrees(table,user,password) 
    return jsonify([d.to_dict() for d in array]) 


@app.route("/update")
def update_degree_api():
    return update_degree()


@app.route("/delete")
def delete_degree_api():
    return delete_degree()


app.run()
