from flask import Flask
from FactorioCalcWeb.session import SessionManagerClass
def create_app():
    app = Flask(__name__)
    app.secret_key = 'Factorio'
    from .views import main_views
    app.register_blueprint(main_views.bp)
    app.config.factorio_session_manager = SessionManagerClass()
    return app
