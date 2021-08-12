import random

from flask import Flask
from random import randint

app = Flask(__name__)

ran=randint(0,9)


@app.route("/")
def hello_world():
    return f"<h1 style='text-align:center'>Guess the number</h1>" \
           f"<pstyle='text-align:center'> Welcome to the wold of Som the god</p>" \
           f"<img style='text-align:center' src='https://giphy.com/gifs/n7cNUxwoKtWne'>"


@app.route("/<num>")
def check(num):
    global ran
    if int(num)>ran:
        return "<h1 style='text-align:center'>Too high</h1>" \
        "<p style='text-align:center'> Try guessing lower</p>" \
        '<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/VFw74cH3dY2t8EIPgN" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/CuriosityStream-curiositystream-curiosity-stream-get-curious-VFw74cH3dY2t8EIPgN">via GIPHY</a></p>'
    if int(num)<ran:
        return "<h1 style='text-align:center'>Too low</h1>" \
        "<p style='text-align:center'> Try guessing higher</p>" \
        "<img style='text-align:center' src='https://giphy.com/gifs/CuriosityStream-curiositystream-curiosity-stream-get-curious-VFw74cH3dY2t8EIPgN'>"
    if int(num)==ran:
        return "<h1 style='text-align:center'>Congratulations!</h1>" \
        "<p style='text-align:center'> You guessed right</p>" \
        "<img style='text-align:center' src='https://giphy.com/gifs/n7cNUxwoKtWne'>"


if __name__ == "__main__":
    app.run(debug=True)

