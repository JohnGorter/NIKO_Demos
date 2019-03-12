from flask import Flask
app = Flask(__name__)

@app.route("/john")
def hello():
    return "Hello NIKO!"