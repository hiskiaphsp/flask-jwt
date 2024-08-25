from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(Config)
    app.config['WTF_CSRF_ENABLED'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    csrf.init_app(app) 

    with app.app_context():
        # Daftarkan blueprint API dan Front-End
        from .routes import api_bp, frontend_bp
        app.register_blueprint(api_bp)
        app.register_blueprint(frontend_bp)

    return app
