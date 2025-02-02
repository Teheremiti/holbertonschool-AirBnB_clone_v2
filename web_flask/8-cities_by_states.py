#!/usr/bin/python3
"""HBNB Flask module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_cities_by_states():
    """Displays an HTML page with the list of all State objects"""
    states_list = storage.all(State)
    return render_template("8-cities_by_states.html", states=states_list)


@app.teardown_appcontext
def teardown():
    """Will remove the current session after the each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
