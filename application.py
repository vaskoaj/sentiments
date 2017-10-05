from flask import Flask, redirect, render_template, request, url_for

import os
import sys
import nltk
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    positive, negative, neutral = 0.0, 0.0, 0.0

    # analyze each tweet separately
    for tweet in tweets:
        score = analyzer.analyze(tweet)

        #increments positive score for positive tweets
        if score > 0.0:
            positive += 1

        #imcrements negative score for negative tweets
        elif score < 0.0:
            negative += 1

        #increments neutral score for neutral tweets
        else:
            neutral +=1


    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
