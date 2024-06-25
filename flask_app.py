from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Darkness, my old friend!"

if __name__ == "main":
    app.run(port=5000, debug=True)

