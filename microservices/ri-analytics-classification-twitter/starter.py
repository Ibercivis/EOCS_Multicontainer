"""This file starts the microservice"""
import os

#!flask/bin/python
from flask import Flask, json, jsonify, logging, request
from flask_cors import CORS, cross_origin


import classification_facade

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


###########################
# receives a json payload containing a list of tweets
#   the payload json has to contain at least a list of tweets of which each contains at least the following fields:
#       text      : string
#       status_id : string
# processes and classifies the raw tweets
# classifies the processed data
###########################


@app.route("/hitec/classify/domain/tweets/lang/<string:lang>", methods=["POST"])
def post_classification_result(lang):
    app.logger.debug('/hitec/classify/domain/tweets/lang/{} called'.format(lang))

    # app.logger.debug(request.data.decode('utf-8'))
    tweets = json.loads(request.data.decode('utf-8'))
    processed_tweets = classification_facade.process_tweets(tweets, lang)

    # app.logger.debug(classified_tweets)
    return jsonify(processed_tweets)


if __name__ == "__main__":
    app.run(debug=False, threaded=False, host="0.0.0.0", port=9655)
