from flask import Flask
from flask_cors import CORS
from FactorioCalcAPI.session import SessionManagerClass
from flask_restx import Api, Resource

app = Flask(__name__)
CORS(app)
api = Api(app)
app.secret_key = 'Factorio'

app.config['JSON_SORT_KEYS'] = False
factorio_session_manager = SessionManagerClass()

import FactorioCalcAPI.main
