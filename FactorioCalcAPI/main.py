from FactorioCalcAPI import api, Resource, factorio_session_manager
from flask import jsonify, request

@api.route('/session')
class InitialSessionCreate(Resource):
    def post(self):
        rand_id = request.json.get('rand_id')
        factorio_session_manager.add_session(rand_id=rand_id)
        return 'session_set'


@api.route('/session/imalive')
class SessionKeepAlive(Resource):
    def post(self):
        rand_id = request.json.get('rand_id')
        if factorio_session_manager.SD.get(rand_id) is not None:
            factorio_session_manager.im_alive(rand_id=rand_id)
            return 'ok'
        else:
            return 'not ok'


@api.route('/api/calc')
class CalcController(Resource):
    def post(self):
        rand_id = request.json.get('rand_id')
        calc_instance = factorio_session_manager.SD.get(rand_id).calc_instance
        refreshed_info = calc_instance.handle_request(request.get_json())
        return jsonify(refreshed_info)


@api.route('/api/recipe_list')
class GetRecipeList(Resource):
    def get(self):
        from FactorioCalcAPI.static_api_handler import get_recipe_list
        return jsonify(get_recipe_list())


@api.route('/api/recipe/<string:name>')  # url pattern으로 name 설정
class GetRecipeSpecific(Resource):
    def get(self, name):  # 멤버 함수의 파라미터로 name 설정
        from FactorioCalcAPI.static_api_handler import get_recipe
        to_return = get_recipe(name)
        return jsonify(to_return)
