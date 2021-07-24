from FactorioCalcAPI import app
from flask import jsonify, request
from FactorioCalcAPI.session import SessionManagerClass


# @app.route('/')
# def main():
#     return ''

@app.route('/session', methods=['POST'])
def initial_session_create():
    rand_id = request.get_json()['rand_id']
    sm_instance: SessionManagerClass = app.config.factorio_session_manager
    if rand_id not in sm_instance.SD.keys():
        sm_instance.add_session(rand_id=rand_id)
    return 'session_set'


@app.route('/session/imalive', methods=['POST'])
def session_keep_alive():
    rand_id = request.get_json()['rand_id']

    sm_instance: SessionManagerClass = app.config.factorio_session_manager
    if sm_instance.SD.get(rand_id) is not None:
        sm_instance.im_alive(rand_id=rand_id)
        return 'ok'
    else:
        return 'not_ok'


@app.route('/api', methods=['POST'])
def calc_controller():
    to_toss = request.get_json()
    rand_id = to_toss['rand_id']
    sm_instance: SessionManagerClass = app.config.factorio_session_manager
    calc_instance = sm_instance.SD.get(rand_id).calc_instance
    refreshed_info = calc_instance.handle_request(to_toss)
    return jsonify(refreshed_info)


@app.route('/api/recipe_list', methods=['GET'])
def common():
    from FactorioCalcAPI.api_handler import get_recipe_list

    return jsonify(get_recipe_list())
