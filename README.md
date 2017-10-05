#Sentiments

Sentiments is an app designed for Twitter. This application uses a web development framework called flask.

Each file uses Twitter's API to take tweets from a provided username. For each tweet, the words are analyzed and compared against accepted positive and negative words. If the tweet contains more of the positive words than negative words then it will return a positive score and vise versa.

Smile is a short code that displays the overall sentiment with emojis in the command-line.

Tweets does a little bit more and displays the score and text of tweet in the command-line.

Application.py uses the web interface to get a user provided Twitter account and provide a pie chart reflecting the sentiments of the last 50 Tweets.
