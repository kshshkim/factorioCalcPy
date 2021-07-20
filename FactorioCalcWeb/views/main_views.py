from flask import Blueprint, render_template, request, current_app, session
from FactorioCalcBase.calculator_base import FactorioCalculatorBase
from FactorioCalcWeb.session import SessionManagerClass

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def main():
    fcb = FactorioCalculatorBase()
    return render_template('test.html')

@bp.route('/session', methods=['POST'])
def initial_session_create():
    rand_id = request.form.get("random_id")
    sm_instance: SessionManagerClass = current_app.config.factorio_session_manager
    sm_instance.add_session(rand_id=rand_id)
    return str(sm_instance.SD.keys())

@bp.route('/session/imalive', methods=['POST'])
def session_keep_alive():
    rand_id = request.form.get("random_id")
    sm_instance: SessionManagerClass = current_app.config.factorio_session_manager
    if sm_instance.SD.get(rand_id) is not None:
        sm_instance.im_alive(rand_id=rand_id)
        return 'ok'
    else:
        return 'not_ok'
