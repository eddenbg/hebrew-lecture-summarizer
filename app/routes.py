from flask import Blueprint

# Create a blueprint for the main routes of the app
main = Blueprint('main', __name__)


@main.route('/')
def index():
    # This route responds to the root URL '/'
    return "Welcome to the Speech Recognition App!"
