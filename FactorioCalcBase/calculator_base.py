from production_block import ProductionBlock
from production_machine import ProductionMachine
from dependency_tracker import DependencyDictMerged
from recipe_class import RecipeClass
import json


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
        self.main_block_obj: ProductionBlock = self.block_obj_dict['general_recipe'].get(recipe_name)
        if self.main_block_obj is None:
            self.main_block_obj: ProductionBlock = self.block_obj_dict['oil_recipe'].get(recipe_name)

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
        specific_block = self.production_block_recipe_finder(recipe_name, 'b')

        if specific_block is not None:
            specific_block.set_module(module_code_or_list)
            self.update_resource_consumption_dict(specific_block)

    def update_total_recipe_dict(self):
        new_obj = DependencyDictMerged(self.recipe_name, self.amount, self.resource_consumption_dict)
        self.total_recipe_dict = new_obj.merged_recipe_dict
        return new_obj.merged_recipe_dict

    def get_block_needed_amount_in_ref_time(self, recipe_name):
        # 기준 시간은 메인 아이템이 하나 만들어지는데 걸리는 시간, 모든 재료*요구량은 기준 시간 내에 생산이 되어야함. 기준 시간 내에 생산 가능한 공장(블록)의 수를 구해야함.
        # 블록(공장) 필요량 = 생산해야할 수량 * 레시피 하나 생산에 걸리는 시간 / 기준시간

        block_obj = self.production_block_recipe_finder(recipe_name=recipe_name, block_or_recipe='b')

        if block_obj == self.main_block_obj:
            block_needed = self.amount
        else:
            ref_time = self.main_block_obj.production_time_per_recipe
            recipe_name = block_obj.recipe_name
            block_obj_production_time = block_obj.production_time_per_recipe
            needed_amount = self.production_block_recipe_finder(recipe_name=recipe_name, block_or_recipe='r')
            block_needed = needed_amount*block_obj_production_time/ref_time
        return block_needed

    def production_block_recipe_finder(self, recipe_name, block_or_recipe: str):
        if block_or_recipe == 'b':
            to_search = self.block_obj_dict
        elif block_or_recipe == 'r':
            to_search = self.total_recipe_dict
        else:
            to_search = None

        target = None

        if to_search is not None:
            for cat in to_search:
                possible_target = to_search[cat].get(recipe_name)
                if to_search[cat].get(recipe_name) is not None:
                    target = possible_target

        return target

    def json_out_total_info(self):
        self.update_total_recipe_dict()
        main_dict = self.total_recipe_dict
        to_return_dict = {}
        for cat in main_dict.keys():
            to_return_dict[cat] = {}
            for recp in main_dict[cat].keys():
                block_obj: ProductionBlock = self.production_block_recipe_finder(recipe_name=recp, block_or_recipe='b')
                amount_required = self.get_block_needed_amount_in_ref_time(recp)
                amount_recipe_required = self.production_block_recipe_finder(recipe_name=recp, block_or_recipe='r')
                to_return_dict[cat][recp] = {
                    'name': recp,
                    'machine_name': block_obj.machine_obj.machine_name,
                    'added_modules': block_obj.module_list,
                    'amount_recipe_required': amount_recipe_required,
                    'amount_factory_required': amount_required,
                    'total_power_consumption': amount_required*block_obj.power_consumption,
                }
        return json.dumps(to_return_dict, sort_keys=False, indent=6)
