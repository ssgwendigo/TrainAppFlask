from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['WMATA_PRIMARY_API_KEY'] = os.getenv('WMATA_PRIMARY_API_KEY')
    app.config['WMATA_SECONDARY_API_KEY'] = os.getenv('WMATA_SECONDARY_API_KEY')

    # Root endpoint
    @app.route('/')
    def version():
        return jsonify({"version": "1.0.0"})

    # Register blueprints
    from app.controllers.station_controller import station_bp
    from app.controllers.train_controller import train_bp
    app.register_blueprint(station_bp)
    app.register_blueprint(train_bp)

    return app