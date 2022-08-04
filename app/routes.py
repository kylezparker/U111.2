from flask import Flask # we imported Flask class from flask module

app = Flask(__name__)  #is an instance

# dracula indent rainbow
# app.get/app.route
@app.get("/") #this is a route
def index(): # our view function
    return "<h1>Hello World</h1>" #return string

@app.get("/about")
def about():
    me={
        "first_name":"kyle",
        "middle_inital":"z",
        "last_name":"parker",
        "age": "unknown",
        "location": "unknown",
        "favorite_food": "unknown",
        "active": True
    }
    return me



# sudo apt update, then upgrade
# sue apt install zsh