from flask import Blueprint, render_template, request, current_app, session
from FactorioCalcBase.calculator_base import FactorioCalculatorBase
from FactorioCalcWeb.session import SessionManagerClass

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'

@bp.route('/dd')
def dd():
    fcb = FactorioCalculatorBase()
    new_dict=fcb.total_info_out_as_dict()
    # return render_template('question_list.html', new_dict=new_dict)
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