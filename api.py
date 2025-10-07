from flask import Flask
from dao_degree import create_table, show_table, update_table, delete_table

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>DEGREES MANAGER</h1>"


@app.route("/insert")
def insert_degree():
    return insert_degree()


@app.route("/show")
def show_degrees():
    return show_degrees()


@app.route("/update")
def update_degree():
    return update_degree


@app.route("/delete")
def delete_degree():
    return delete_degree()


app.run()
