from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    print(request.method)
    return "login page"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
