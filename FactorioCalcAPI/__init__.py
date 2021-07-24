from flask import Flask
from flask_cors import CORS
from FactorioCalcAPI.session import SessionManagerClass

app = Flask(__name__)
CORS(app)
app.secret_key = 'Factorio'

app.config['JSON_SORT_KEYS'] = False
app.config.factorio_session_manager = SessionManagerClass()

import FactorioCalcAPI.main
