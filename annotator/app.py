from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from annotator.config import Categories, Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    static_folder=os.path.join(basedir, "statics"),
    template_folder=os.path.join(basedir, "templates")
)

db = SQLAlchemy()

import annotator.routes
import annotator.cli


@app.context_processor
def inject_dict_for_all_templates():
    return dict(categories=Categories)


def init_app(config: Config=None):
    if not config:
        config = Config
    app.config.from_object(config)
    db.init_app(app)

    return app
