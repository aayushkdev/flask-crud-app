from flask import Flask
from core.extensions import mongo, ma
from core.db.init_db import initialize_indexes

def create_app():
    app = Flask(__name__)
    app.config.from_object("core.config.Config")

    mongo.init_app(app)
    ma.init_app(app)

    from core.routes.user import user_bp
    from core.errors.handlers import errors_bp

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(errors_bp)

    with app.app_context():
        initialize_indexes()

    return app
