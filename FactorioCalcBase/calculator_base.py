from FactorioCalcBase.production_block import ProductionBlock
from FactorioCalcBase.dependency_tracker import FullDependency
from FactorioCalcBase.recipe import Recipe
import json


class CalculatorBase:
    def __init__(self, recipe_name='advanced-circuit', amount=1, mining_research_modifier=0, extra_product_rate_dict=None, extra_conf=None, preferred_machine_list=None, use_kovarex=False):
        self.recipe_name = recipe_name
        self.recipe_obj = Recipe(self.recipe_name)
        self.amount = amount
        self.mining_research_modifier = mining_research_modifier
        self.use_kovarex = use_kovarex

        self.total_recipe_dict = {}
        self.total_item_dict = {}
        self.total_out_dict = {}

        self.extra_product_rate_dict = extra_product_rate_dict
        if self.extra_product_rate_dict is None:
            self.extra_product_rate_dict = {}
        self.block_obj_dict = {}
        self.node_dict = {}
        self.extra_conf = extra_conf
        self.preferred_machine_list = preferred_machine_list
        if self.preferred_machine_list is None:
            self.preferred_machine_list = []
        self.make_initial_block_objs()

    def make_initial_total_recipe_dict(self):
        new_obj = FullDependency(self.recipe_name, self.amount, self.extra_product_rate_dict, use_kovarex=self.use_kovarex)
        self.total_recipe_dict = new_obj.merged_recipe_dict
        self.total_item_dict = new_obj.merged_item_dict

    def make_initial_block_objs(self):
        self.make_initial_total_recipe_dict()
        ref_dict = self.total_recipe_dict
        for each_category in ref_dict.keys():
            self.block_obj_dict[each_category] = {}
            for each_recipe in ref_dict[each_category].keys():
                self.block_obj_dict[each_category][each_recipe] = ProductionBlock(recipe_name=each_recipe, mining_research_modifier=self.mining_research_modifier, preferred_machine_list=self.preferred_machine_list)

    def update_extra_product_dict(self, block_obj):
        self.extra_product_rate_dict[block_obj.recipe_name] = block_obj.extra_product_rate

    def set_module_to_specific_block(self, recipe_name, module_code_or_list):
        specific_block = self.production_block_recipe_finder(recipe_name=recipe_name, block_or_recipe='b')

        if specific_block is not None:
            specific_block.set_module(module_code_or_list)
            self.update_extra_product_dict(specific_block)

    def set_module_to_all_blocks(self, module_code_or_list):
        for each_production_block in self.block_obj_dict.values():
            each_production_block.set_module(module_code_or_list)
            self.update_extra_product_dict(each_production_block)

    def change_machine_to_specific_block(self, recipe_name: str, machine_name: str):
        specific_block: ProductionBlock = self.production_block_recipe_finder(recipe_name=recipe_name, block_or_recipe='b')

        if specific_block is not None and type(machine_name) == str:
            specific_block.update_machine(machine_name)

    def update_total_recipe_dict(self):
        new_obj = FullDependency(self.recipe_name, self.amount, self.extra_product_rate_dict, use_kovarex=self.use_kovarex)
        self.total_recipe_dict = new_obj.merged_recipe_dict
        self.total_item_dict = new_obj.merged_item_dict

    def get_block_needed_amount_in_ref_time(self, recipe_name):
        # 기준 시간은 메인 아이템이 하나 만들어지는데 걸리는 시간, 모든 재료*요구량은 기준 시간 내에 생산이 되어야함. 기준 시간 내에 생산 가능한 공장(블록)의 수를 구해야함.
        # 블록(공장) 필요량 = 생산해야할 수량 * 레시피 하나 생산에 걸리는 시간 / 기준시간

        block_obj = self.production_block_recipe_finder(recipe_name=recipe_name, block_or_recipe='b')
        main_block_obj = self.production_block_recipe_finder(recipe_name=self.recipe_name, block_or_recipe='b')
        if block_obj == main_block_obj:
            block_needed = self.amount
        else:
            ref_time = main_block_obj.production_time_per_recipe
            recipe_name = block_obj.recipe_name
            block_obj_production_time = block_obj.production_time_per_recipe
            needed_amount = self.production_block_recipe_finder(recipe_name=recipe_name, block_or_recipe='r')
            block_needed = needed_amount*block_obj_production_time/ref_time
        return block_needed

    def production_block_recipe_finder(self, recipe_name: str, block_or_recipe: str):
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

    def total_info_out_as_dict(self):
        self.update_total_recipe_dict()
        main_dict = self.total_recipe_dict
        to_return_dict = {}
        for cat in main_dict.keys():
            to_return_dict[cat] = {}
            for recp in main_dict[cat].keys():  # 카테고리를 분리해서 출력할 경우 필요한 코드, 현재는 필요하지 않지만 성능 영향이 크지 않아서 그냥 둠.
                block_obj: ProductionBlock = self.production_block_recipe_finder(recipe_name=recp, block_or_recipe='b')
                amount_factory_required = self.get_block_needed_amount_in_ref_time(recp)
                amount_recipe_required = self.production_block_recipe_finder(recipe_name=recp, block_or_recipe='r')
                to_return_dict[cat][recp] = {
                    'name': recp,
                    'product_per_a_minute': '',
                    'amount_recipe_required': round(amount_recipe_required, 4),
                    'amount_factory_required': round(amount_factory_required, 4),
                    'machine_name': block_obj.machine_obj.machine_name,
                    'added_modules': block_obj.module_list,
                    'speed_rate': block_obj.production_speed,
                    'base_speed_rate': block_obj.machine_obj.base_speed_rate,
                    'total_power_consumption': round(amount_factory_required*block_obj.power_consumption, 4),
                }
        to_return_dict['items'] = self.total_item_dict
        self.total_out_dict = to_return_dict
        return to_return_dict

    def change_amount(self, amount: float):
        self.amount = amount

    def json_out(self):
        return json.dumps(self.total_info_out_as_dict(), sort_keys=False, indent=4)

    def diagram_data_out(self):
        node_list = list(self.total_recipe_dict['recipe'].keys())
        t_and_s_list = []

        def update_t_and_s_list(source, itm_name):
            if itm_name != self.recipe_name:
                try:
                    required_by_dict = self.total_item_dict[itm_name]['required_by']
                except KeyError:  # 잉여생산물이 필요한 노드가 없어서 오류 발생
                    required_by_dict = {}
                for target, strength in required_by_dict.items():
                    t_and_s_list.append((source, itm_name, target, strength))

        for node in node_list:
            key_list = list(Recipe(node).results.keys())
            for key in key_list:
                update_t_and_s_list(node, key)

        link_dict = {
            'source': [],
            'target': [],
            'value': [],
            'label': [],
            'node': node_list,
            'node_value': [],
            'node_custom_data': [],
            'link_custom_data': []
        }
        for node in node_list:
            link_dict['node_custom_data'].append(f'"{self.total_out_dict["recipe"][node]["machine_name"]}" x{str(self.total_out_dict["recipe"][node]["amount_factory_required"])}"')
        for source, itm_name, target, strength in t_and_s_list:
            link_dict['source'].append(node_list.index(source))
            link_dict['target'].append(node_list.index(target))
            if itm_name in ['water', 'crude-oil', 'petroleum-gas', 'light-oil', 'heavy-oil']:
                link_dict['value'].append(strength/10)
            else:
                link_dict['value'].append(strength)
            link_dict['label'].append(itm_name)
            link_dict['node_value'].append(self.total_recipe_dict['recipe'][source])
            link_dict['link_custom_data'].append(f'total "{str(strength)}" of "{itm_name}" required by "{target}"')
        return link_dict
