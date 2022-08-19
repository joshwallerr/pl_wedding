from flask import Flask, render_template, request, jsonify, make_response, redirect
import sqlite3
import psycopg2

app = Flask(__name__)

# 8 Min into video - https://www.youtube.com/watch?v=CHRikEvvcUc

# REMEMBER TO STORE IN DB BEFORE PUBLISHING !!!!

POSTGRESQL_URI = "postgres://kmzcqmqm:XeQGdYSZCdE44pOokU1Uks38hb1A6mYu@tyke.db.elephantsql.com/kmzcqmqm"

try:
    connection = psycopg2.connect(POSTGRESQL_URI)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE messages (message TEXT, sender TEXT);"
            )
except psycopg2.errors.DuplicateTable:
    pass


@app.route("/", methods=["POST", "GET"])
def index():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM messages;")
            messages = cursor.fetchall()

    return render_template("index.html", messages=messages)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    return render_template("submit.html")


@app.route("/submit/process", methods=["POST", "GET"])
def submit_process():
    if request.method == 'POST':
        print(request.form.get("message"))
        print(request.form.get("from"))

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO messages VALUES(%s, %s)",
                    (
                        request.form.get("message"),
                        request.form.get("from"),
                    ),
                )

    # print(messages)
    return redirect("/success")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run()