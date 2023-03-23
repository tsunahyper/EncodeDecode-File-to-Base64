# Importing the necessary modules and libraries
from flask import Flask, request
import os
from routes.blueprint import blueprint

def create_app():
    app = Flask(__name__)  # flask app object

    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/bp')

if __name__ == '__main__':  # Running the app
    app.run()