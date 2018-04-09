from flask import render_template
from app import app

@main.errorhandler(404)
def four_Ow_four(error):
    return render_template('fourOwfour.html'),404
