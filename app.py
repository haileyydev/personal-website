from src.backend.flask_app import run_flask_server
import config

if __name__ == "__main__":
    run_flask_server(config.FLASK_HOST, config.FLASK_PORT)