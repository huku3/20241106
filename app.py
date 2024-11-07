from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hi onodera"


@app.route("/goodbye")
def goodbye():
    return "GoodBye"


@app.route("/user/<name>")
def hi(name):
    return f"Hi, {name}!"


@app.route("/about/<name>")
def about(name):
    return f"{name}'s profile"


@app.route("/hello")
def hello():
    return "<html><body><h1>Hello</h1></body></html>"


@app.route("/profile/<name>")
def profile(name):
    html = f"<html><body><h1>{name}'s profile Hello</h1></body></html>"
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
