#!/usr/bin/python3
"""HBNB Flask module"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def display_page():
    """Displays the HTML page of the HBNB"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown():
    """Will remove the current session after the each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
