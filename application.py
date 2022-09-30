from flask import Flask
application = Flask(__name__)



@application.route("/")
def index():
    return "moon"



@application.route("/hello")
def hello():
    return "Hello World!f"
