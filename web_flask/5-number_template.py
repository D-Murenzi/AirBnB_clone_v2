#!/usr/bin/python3
"""THis script contains some routes."""

from flask import Flask, render_template


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


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_greeting(text='is cool'):
    """Check for default arg task."""
    return "Python {:s}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    """Display a number if its an int."""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return a template html page."""
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
