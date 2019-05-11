from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from annotator.config import Categories, Config

app = Flask(__name__)
db = SQLAlchemy()

import annotator.routes
import annotator.cli


def init_app(config: Config=None):
    if not config:
        config = Config
    app.config.from_object(config)
    db.init_app(app)

    return app
