from flask import Flask
application = Flask(__name__)



@application.route("/")
def index():
    return "Hi"



@application.route("/hello")
def hello():
    return "Hello World!f"
