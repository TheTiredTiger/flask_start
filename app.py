from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def whatever():
    return "hiya"

@app.route("/user/<username>")
def show_user(username):
    return f"User {username}"

@app.route("/user", methods=["POST"])
def peeps():
    body = request.get_json()
    if body is None:
        return "Nope, not here", 400
    if "first_name" not in body:
        return "Write your first name down this instant or so help me", 400
    if "last_name" not in body:
        return "Somebody is missing something. Write your last name!"

    return body, 200

@app.route("/json", methods=["GET", "POST"])
def another():
    content = {
        "name": "depression",
        "age": "as old as time"
    }

    response = jsonify(content)
    return content["age"]




app.run(host = "0.0.0.0", port=9191)