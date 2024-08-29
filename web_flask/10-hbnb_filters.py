#!/usr/bin/python3
"""This module starts a webappliaction that displays states."""

from flask import Flask, render_template
from models import storage


app = Flask(__name__, template_folder='/home/davidm/AirBnB_clone_v2/web_flask/static/')


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """Filter according to hbnb requirements."""
    States= storage.all('State')
    Amenities = storage.all('Amenity')
    return render_template('6-index.html', states=States, amenities=Amenities)


@app.teardown_appcontext
def close(exception=None):
    """Close the db session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
