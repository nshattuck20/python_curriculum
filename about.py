from flask import Blueprint, render_template 

about_blueprint = Blueprint('about', __name__, template_folder='templates')


@about_blueprint.route('/')
def about():
    return render_template('about.html')