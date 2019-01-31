#!/usr/bin/env python
__author__ = "mdshepard"

from flask import Flask, render_template
from tinydb import TinyDB
import random

app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/')
def random_recipe():
    """The route decorator specifies the destination of the template.
    db.all() retrieves the data from the database in the form of a dictionary
    with the keys being the columns and the values being the rows.
    random.choice() selects a table from the db at random, it is returned and
    rendered to the template"""
    recipe_dict = db.all()
    recipe = random.choice(recipe_dict)
    return render_template('template.html', recipe=recipe)


if __name__ == "__main__":
    pass
