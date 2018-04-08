from flask import Flask

# Initializing application
app = Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig)

from app import views
