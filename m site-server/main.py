from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nameplate")
def contact():
    return render_template("nameplate.html")


if __name__=="__main__":
    app.run()
