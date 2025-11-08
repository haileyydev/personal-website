from flask import Blueprint, render_template

blueprint = Blueprint('pages', __name__)

# The main route that serves the website
@blueprint.route('/')
def index():
    return render_template('index.html')