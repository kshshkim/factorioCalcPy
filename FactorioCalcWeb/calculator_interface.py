from FactorioCalcBase.calculator_base import FactorioCalculatorBase

available_action_list = ['initial_info', 'change_config', 'set_module_to_specific_block', 'change_machine_to_specific_block']

class CalcInstance:
    def __init__(self):
        self.base_obj = FactorioCalculatorBase()
        self.config = {
            'recipe_name': 'advanced-circuit',
            'recipe_amount': '1',
            'mining_research_modifier': None,
        }

    def initialize_base_obj(self):
        recipe_name = self.config['recipe_name']
        recipe_amount = self.config['recipe_amount']
        mining_research_modifier = self.config['mining_research_modifier']
        self.base_obj = FactorioCalculatorBase(recipe_name=recipe_name, amount=recipe_amount, mining_research_modifier=mining_research_modifier)

    def change_config(self, instruction: dict):
        self.config.update(instruction)
        self.initialize_base_obj()

    def handle_request(self, json_data: dict):
        # example of json_data
        # example = {
        #     "rand_id": 0.12345,
        #     "action": {
        #         0: {
        #             "action_name": "change_config",
        #             "recipe_name": "processing-unit",
        #             "recipe_amount": "10",
        #             "mining_research_modifier": 0.3
        #         }
        #     }
        # }
        action_dict: dict = json_data['action']
        for each_action in action_dict.keys():
            current_action_name = action_dict[each_action]['action_name']
            current_action_dict: dict = action_dict[each_action]
            self.do_action(action_name=current_action_name, action_dict=current_action_dict)
        return self.base_obj.total_info_out_as_dict()  # 요청 처리 후 결과값 새로고침, 딕셔너리로 반환

    def do_action(self, action_name: str, action_dict: dict):
        if action_name in available_action_list:
            if action_name == 'change_config':
                self.change_config(action_dict)
            elif action_name == 'set_module_to_specific_block':
                recipe_name = action_dict['recipe_name']
                module_list = action_dict['module_list']
                self.base_obj.set_module_to_specific_block(recipe_name=recipe_name, module_code_or_list=module_list)
            elif action_name == 'change_machine_to_specific_block':
                recipe_name = action_dict['recipe_name']
                machine_name = action_dict['machine_name']
                self.base_obj.change_machine_to_specific_block(recipe_name=recipe_name, machine_name=machine_name)
