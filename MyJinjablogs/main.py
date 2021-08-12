from flask import Flask,render_template
import datetime
import requests

app=Flask(__name__)
year=datetime.datetime.now().year


@app.route("/")
def home():
    global year
    return render_template("index.html",year=year)

@app.route("/<username>")
def guess(username):
    global year
    agify = f"https://api.agify.io?name={username}"
    genderify = f"https://api.genderize.io?name={username}"
    nationality = f"https://api.nationalize.io?name={username}"

    agify_response = requests.get(url=agify)
    a = agify_response.json()
    genderify_response = requests.get(url=genderify)
    g = genderify_response.json()
    nationality_response = requests.get(url=nationality)
    n = nationality_response.json()

    age = a['age']
    gender = g['gender']
    gender_probablity = g['probability']
    c_id = [con['country_id'] for con in n['country']]
    countries = ""
    for _ in c_id:
        countries = countries + " " + str(_)
    return render_template("guess.html",name=username,year=year,genderP=gender_probablity,gender=gender,age=age,countries=countries)

@app.route("/blog")
def get_blog():
    blog_url="https://api.npoint.io/465e632a9083f27da735"
    response=requests.get(url=blog_url)
    return render_template("blog.html",blog_posts=response.json())



if __name__=="__main__":
    app.run(debug=True)
