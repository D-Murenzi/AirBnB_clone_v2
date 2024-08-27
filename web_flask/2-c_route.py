#!/usr/bin/python3
"""THis script contains some routes."""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Say hello."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNBH."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def replace(text):
    """Return c and a text."""
    return "C {:s}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
