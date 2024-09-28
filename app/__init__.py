from flask import Flask


def create_app():
    # Create a new Flask application
    app = Flask(__name__)

    # Import the routes defined in routes.py and register them with the app
    from .routes import main
    app.register_blueprint(main)

    return app
