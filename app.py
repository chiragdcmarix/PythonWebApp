from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a first file and  sample Python Web App running on Flask Framework!"
    return " This is also form Devops team and IT team"

