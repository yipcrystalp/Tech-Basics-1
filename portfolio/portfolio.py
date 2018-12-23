from flask import Flask, render_template, request, url_for
import os




app = Flask(__name__)


posts = [

    {

        'artist': 'Crystal Yip',
        'title': 'Art Works',
        'content': 'Scroll down for more :)',
        'date_posted': '2016-2018'
    }


]



@app.route("/")
def home():
    return render_template('home.html', posts=posts,)


if __name__ == "__main__":
    app.run(debug=True)
