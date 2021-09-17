from FactorioCalcBase.calculator_base import FactorioCalculatorBase


class Calculator:
    def __init__(self, conf):
        self.conf = conf
        self.base = None
        self.results = {}
        self.diagram_data = None
        self.dd = None
        self.initialize_base_obj()

    def initialize_base_obj(self):
        recipe_name = self.conf.recipe_name
        amount = self.conf.amount
        mining_research_modifier = self.conf.mining_research_modifier
        preferred_machine_list = self.conf.preferred_machine_list
        use_kovarex = self.conf.use_kovarex
        self.base = FactorioCalculatorBase(recipe_name=recipe_name, amount=amount,
                                           mining_research_modifier=mining_research_modifier,
                                           preferred_machine_list=preferred_machine_list,
                                           use_kovarex=use_kovarex
                                           )
        self.update_result()

    def change_amount(self, amount):
        self.base.change_amount(amount)

    def change_machine(self, recipe_name: str, machine_name: str):
        self.base.change_machine_to_specific_block(recipe_name=recipe_name, machine_name=machine_name)

    def set_module(self, recipe_name: str, module_list: list):
        self.base.set_module_to_specific_block(recipe_name=recipe_name, module_code_or_list=module_list)

    async def async_update_result(self):
        self.results = self.base.total_info_out_as_dict()

    def update_result(self):
        self.results = self.base.total_info_out_as_dict()

    def parse_action(self, action):
        if action.action_name == 'change_machine':
            recipe_name = action.action_detail.get('recipe_name')
            machine_name = action.action_detail.get('machine_name')
            self.change_machine(recipe_name=recipe_name, machine_name=machine_name)
        elif action.action_name == 'set_module':
            recipe_name = action.action_detail.get('recipe_name')
            module_list = action.action_detail.get('module_list')
            self.set_module(recipe_name=recipe_name, module_list=module_list)
        elif action.action_name == 'change_amount':
            amount = action.action_detail.get('amount')
            self.change_amount(amount=amount)

    async def diagram_data_update(self):
        self.diagram_data = self.base.diagram_data_out()
        from FactorioCalcBase.dependency_diagram import DependencyDiagram
        self.dd = DependencyDiagram(self.conf, self.base.diagram_data_out())
        return self.dd.get_html()
