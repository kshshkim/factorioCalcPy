from production_block import ProductionBlock
from production_machine import ProductionMachine
from dependency_tracker import DependencyDictMerged
from recipe_class import RecipeClass


class FactorioCalculatorBase:
    def __init__(self, recipe_name='advanced-circuit', amount=1, mining_research_modifier=0, resource_consumption_dict=None):
        self.recipe_name = recipe_name
        self.recipe_obj = RecipeClass(self.recipe_name)
        self.amount = amount
        self.mining_research_modifier = mining_research_modifier
        self.total_recipe_dict = {}

        self.resource_consumption_dict = resource_consumption_dict
        if self.resource_consumption_dict is None:
            self.resource_consumption_dict = {}
        self.block_obj_dict = {
            'general_recipe': {},
            'oil_recipe': {}
        }
        self.general_obj_dict = self.block_obj_dict['general_recipe']
        self.oil_obj_dict = self.block_obj_dict['oil_recipe']
        self.make_initial_block_objs()

    def make_initial_total_recipe_dict(self):
        new_obj = DependencyDictMerged(self.recipe_name, self.amount, self.resource_consumption_dict)
        self.total_recipe_dict = new_obj.merged_recipe_dict

    def make_initial_block_objs(self):
        self.make_initial_total_recipe_dict()
        ref_dict = self.total_recipe_dict
        for recipe_kind in ref_dict.keys():
            for key in ref_dict[recipe_kind].keys():
                self.block_obj_dict[recipe_kind][key] = ProductionBlock(recipe_name=key, mining_research_modifier=self.mining_research_modifier)

    def update_resource_consumption_dict(self, block_obj):
        self.resource_consumption_dict[block_obj.recipe_name] = block_obj.resource_consumption_rate

    def change_mining_research_modifier(self, mrm):
        self.mining_research_modifier = mrm
        for block_obj in self.block_obj_dict['general_recipe'].values():
            if block_obj.recipe_obj.category == 'mining-drill':
                block_obj.mining_research_modifier = mrm
                block_obj.update_and_calculate_at_once()
                self.update_resource_consumption_dict(block_obj=block_obj)

    def set_module_to_specific_block(self, recipe_name, module_code_or_list):
        specific_block = self.block_obj_dict['general_recipe'].get(recipe_name)
        if specific_block is None:
            specific_block = self.block_obj_dict['oil_recipe'].get(recipe_name)

        if specific_block is not None:
            specific_block.set_module(module_code_or_list)
            self.update_resource_consumption_dict(specific_block)

    def update_total_recipe_dict(self):
        new_obj = DependencyDictMerged(self.recipe_name, self.amount, self.resource_consumption_dict)
        self.total_recipe_dict = new_obj.merged_recipe_dict
        return new_obj.merged_recipe_dict

    def get_how_many_block_needed_dict(self):
        pass