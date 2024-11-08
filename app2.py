from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    # print(request.method)
    if request.method == "GET":
        
        return """
        <form action="/login" method="post">
        Password<input type="text"><br>
        <input type="submit">
        </form>
        """
    else:
        return "logged in"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
