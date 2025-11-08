from flask import Flask
from .routes import pages

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

app.register_blueprint(pages.blueprint)

def run_flask_server(host, port):
    app.run(host=host, port=port, debug=False)