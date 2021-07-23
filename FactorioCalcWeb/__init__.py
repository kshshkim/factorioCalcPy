from flask import Flask, render_template, request, current_app, jsonify
from FactorioCalcWeb.session import SessionManagerClass

app = Flask(__name__)
app.secret_key = 'Factorio'

app.config['JSON_SORT_KEYS'] = False
app.config.factorio_session_manager = SessionManagerClass()

import FactorioCalcWeb.main
