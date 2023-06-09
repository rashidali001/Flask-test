from app import app
from flask import render_template, redirect
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {
        "name":"Rashid"
    }
    posts = [
        {
            "author":"Bikozulu",
            "article":"This is a written blog post by Bikozulu"
        },
        {
            "author":"Eric Thomas",
            "article":"Be you! Be fearless"
        }
    ]

    return render_template("index.html", user=user, posts=posts, title="Home")


@app.route("/login", methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.is_validated():
        return redirect("index")

    return render_template("login.html", form=form, title="login")
