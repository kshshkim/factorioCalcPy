from FactorioCalcBase.calculator_base import FactorioCalculatorBase
from FactorioCalcBase.dependency_tracker import ProcessGeneral
from FactorioCalcBase.dependency_diagram import DependencyDiagram
from FactorioCalcBase.dependency_tracker import FullDependency
import pprint
import json
from FactorioCalcBase.recipe_class import RecipeClass
#
pml = []
ase = FactorioCalculatorBase('big-electric-pole', amount=1, preferred_machine_list=pml, use_kovarex=True)
# ase.set_module_to_specific_block('advanced-oil-processing', ['p1'])
pprint.pp(ase.total_info_out_as_dict())
# pprint.pp(ase.diagram_data_out())

# tstobj = FullDependency('advanced-circuit', 1, {}, False)
# print(tstobj.merged_item_dict)