from flask import Flask
from dao_degree import create_table, show_table, update_table, delete_table

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>DEGREES MANAGER</h1>"


@app.route("/create")
def create_table():
    return create_table()


@app.route("/show")
def show_table():
    return show_table()


@app.route("/update")
def update_table():
    return update_table


@app.route("/delete")
def delete_table():
    return delete_table()


app.run()
