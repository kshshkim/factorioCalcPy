import pprint
from FactorioCalcBase.data.binary import sorted_recipe_list, production_machine_category_list_dict
from FactorioCalcBase.recipe import Recipe
from FactorioCalcBase.calculator_base import CalculatorBase
from FactorioCalcBase.dependency_dict_common_function import dict_add_number
import time


def test_change_machine(test_obj: CalculatorBase, target_recipe, failed_dict):
    recipe_obj = Recipe(recipe_name=target_recipe)
    cat = recipe_obj.get_category()
    available_machine_list = production_machine_category_list_dict.get(cat)
    failed_dict['method_failed']['change_machine_failed'] = {}
    if len(available_machine_list) > 1:
        for machine in available_machine_list:
            test_obj.change_machine_to_specific_block(recipe_name=target_recipe,
                                                      machine_name=machine)
            if test_obj.block_obj_dict['recipe']['machine_name'] != machine:
                raise 'MachineNotChanged'


def test_calculator_base_methods(test_obj: CalculatorBase, failed_dict: dict):

    recipe_list = list(test_obj.block_obj_dict['recipe'].keys())
    for recipe in recipe_list:
        try:
            test_change_machine(test_obj, recipe, failed_dict)
        except:
            dict_add_number(failed_dict['method_failed']['change_machine_failed'], recipe, 1)



def test_calculator_base(failed_dict):
    mrms = [0, 0.3]
    pm = [None, ["assembling-machine-2", "stone-furnace", "burner-mining-drill"]]
    uk = [True, False]
    am = [1, 101.5]

    failed_dict['init_failed'] = {}
    failed_dict['method_failed'] = {
        'change_machine_failed': {

        }
    }
    for recipe in sorted_recipe_list:
        for mining_research_modifier in mrms:
            for preferred_machines in pm:
                for use_kovarex in uk:
                    for amount in am:
                        try:
                            test_obj = CalculatorBase(recipe_name=recipe, amount=amount,
                                                      preferred_machine_list=preferred_machines,
                                                      use_kovarex=use_kovarex,
                                                      mining_research_modifier=mining_research_modifier)
                        except:
                            dict_add_number(failed_dict['init_failed'], key=recipe, val=1)
                        test_calculator_base_methods(test_obj, failed_dict)
    pprint.pp(failed_dict)
    return failed_dict

start_time = time.time()
test_calculator_base({})
print(f'finished in {time.time()-start_time}')
