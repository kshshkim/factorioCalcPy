from FactorioCalcBase.calculator_base import FactorioCalculatorBase
from FactorioCalcBase.dependency_tracker import DependencyTracker
import pprint
import json
from FactorioCalcBase.recipe_class import RecipeClass
#
ase = FactorioCalculatorBase('nuclear-fuel', amount=1)
ase.set_module_to_specific_block('advanced-oil-processing', ['p1'])
pprint.pp(ase.total_info_out_as_dict())
