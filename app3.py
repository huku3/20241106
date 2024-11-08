from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/fruits")
def fruits():
    fruits = ["apple", "banana", "cherry"]
    return render_template("fruits.html", fruits=fruits)


@app.route("/season")
def season():
    month = random.randint(1, 12)
    return render_template("season.html", month=month)


@app.route("/addition/<int:num1>/<float:num2>")
def addition(num1, num2):
    
    result = int(num1) + num2
    return render_template("addition.html", result=result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
