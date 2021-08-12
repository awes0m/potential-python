from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def inner():
        a=function()
        return f"<b> {a} </b>"
    return inner

def make_italc(function):
    def inner():
        a=function()
        return f"<em> {a} </em>"
    return inner

def make_underlined(function):
    def inner():
        a=function()
        return f"<u> {a} </u>"
    return inner

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
           "<p> Welcome to the wold of Som the god</p>"

@app.route("/bye")
@make_bold
@make_underlined
@make_italc
def bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name}! ✌"

@app.route("/debug")
def bugger():
   return f"debugger is working"

if __name__=="__main__":
    app.run(debug=True)

