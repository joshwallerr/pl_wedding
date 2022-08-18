from flask import Flask, render_template, request, jsonify, make_response
import sqlite3

app = Flask(__name__)

# 8 Min into video - https://www.youtube.com/watch?v=CHRikEvvcUc

# REMEMBER TO STORE IN DB BEFORE PUBLISHING !!!!
messages = [
    ("Hope you have a great day!", "Jsh WAller"),
    ("Hope you have a epic day!", "big man"),
    ("Hope you have a nice day!", "grandma"),
]

@app.route("/")
def index():
    message = {'message': "Have a great day!", 'from': "Josh"}
    return render_template("index.html", messages=messages)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == 'POST':
        print(request.form.get("message"))
        print(request.form.get("from"))

        messages.append(
            (
                request.form.get("message"),
                request.form.get("from"),
            )
        )

    return render_template("submit.html")


if __name__ == "__main__":
    app.run()