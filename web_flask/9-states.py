#!/usr/bin/python3
"""This module starts a webappliaction that displays states."""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_only():
    """Return a state template."""
    state_list = storage.all('State')
    return render_template('8-cities_by_states.html', state=state_list)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Return a specific state."""
    state_list = storage.all('State')
    for state in state_list.values():
        if state.id == id:
            state_id = state
            return render_template('9-states.html', state=state_id)
        else:
            pass
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def close(exception=None):
    """Close the db session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
