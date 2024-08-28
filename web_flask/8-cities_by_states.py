#!/usr/bin/python3
"""This module returns all states in HBNBH clone database."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def states():
    """Return a list of states in storage."""
    
    state_list = storage.all(State)
    return render_template('8-cities_by_states.html', state=state_list)

@app.teardown_appcontext
def close(exception=None):
    """Close database sessions or file."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
