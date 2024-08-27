#!/usr/bin/python3
"""This script starts a flask app that listens at 0.0.0.0:5000."""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return hello hbnb!."""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
