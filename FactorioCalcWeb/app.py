from flask import Flask, render_template, request, current_app, jsonify
from FactorioCalcWeb.session import SessionManagerClass

app = Flask(__name__)
app.secret_key = 'Factorio'

app.config['JSON_SORT_KEYS'] = False
app.config.factorio_session_manager = SessionManagerClass()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/session', methods=['POST'])
def initial_session_create():
    print(request.get_json())
    rand_id = request.get_json()['rand_id']
    print(rand_id)
    sm_instance: SessionManagerClass = current_app.config.factorio_session_manager
    if rand_id not in sm_instance.SD.keys():
        sm_instance.add_session(rand_id=rand_id)
    return 'session_set'


@app.route('/session/imalive', methods=['POST'])
def session_keep_alive():
    print(request.get_json())
    rand_id = request.get_json()['rand_id']

    sm_instance: SessionManagerClass = current_app.config.factorio_session_manager
    if sm_instance.SD.get(rand_id) is not None:
        sm_instance.im_alive(rand_id=rand_id)
        return 'ok'
    else:
        return 'not_ok'


@app.route('/api', methods=['POST'])
def calc_controller():
    to_toss = request.get_json()
    rand_id = to_toss['rand_id']
    sm_instance: SessionManagerClass = current_app.config.factorio_session_manager
    refreshed_info = sm_instance.SD[rand_id].calc_instance.handle_request(to_toss)
    return jsonify(refreshed_info)


if __name__ == "__main__":
     app.run()
