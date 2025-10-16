from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    from .routes import nba, mlb, nfl
    app.register_blueprint(nba.bp)
    app.register_blueprint(mlb.bp)
    app.register_blueprint(nfl.bp)

    @app.route("/")
    def index():
        return {"message": "Fantasy Sports API is live!"}

    return app
