from flask import Flask, render_template, request, jsonify, make_response
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    message = {'message': "Have a great day!", 'from': "Josh"}
    return render_template("index.html", message=message)


@app.route("/submit")
def submit():
    return render_template("submit.html")


@app.route("/submit/process", methods=["POST", "GET"])
def submit_process():
    req = request.get_json()

    return make_response(jsonify(req), 200)


if __name__ == "__main__":
    app.run()