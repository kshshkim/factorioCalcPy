from data.production_machine_category_list_dict import production_machine_category_list_dict as pmc_list_dict
from factorio_production_machine_class import FactorioMachine
from factorio_item_class import FactorioItem


class FactorioCalc:
    def __init__(self, item_name='advanced-circuit', mining_research_modifier=0, resource_consumption_modifier_dict=None):
        if resource_consumption_modifier_dict is None:
            resource_consumption_modifier_dict = {}
        self.resource_consumption_modifier_dict = resource_consumption_modifier_dict
        self.item_obj = FactorioItem(item_name, resource_consumption_modifier_dict)
        # 선택 가능 머신 설정
        self.available_machine_list = self.get_available_machine_list()
        self.production_machine_name = self.available_machine_list[0]
        self.to_add_module_list = []
        self.machine_obj = FactorioMachine(self.production_machine_name, self.to_add_module_list, resource_consumption_modifier_dict)
        self.mining_research_modifier = mining_research_modifier

    def get_available_machine_list(self):
        item_category = self.item_obj.get_category()
        machine_list = pmc_list_dict[item_category]
        return machine_list

    def is_able_to_add_a_module(self, module_name: str):
        module_list = ['p1', 'p2', 'p3', 'e1', 'e2', 'e3', 's1', 's2', 's3']
        pmodule_list = [
            'sulfuric-acid',
            'basic-oil-processing',
            'advanced-oil-processing',
            'coal-liquefaction',
            'heavy-oil-cracking',
            'light-oil-cracking',
            'solid-fuel-from-light-oil',
            'solid-fuel-from-heavy-oil',
            'solid-fuel-from-petroleum-gas',
            'lubricant',
            'iron-plate',
            'copper-plate',
            'steel-plate',
            'stone-brick',
            'sulfur',
            'plastic-bar',
            'empty-barrel',
            'uranium-processing',
            'copper-cable',
            'iron-stick',
            'iron-gear-wheel',
            'electronic-circuit',
            'advanced-circuit',
            'processing-unit',
            'engine-unit',
            'electric-engine-unit',
            'uranium-fuel-cell',
            'explosives',
            'battery',
            'flying-robot-frame',
            'low-density-structure',
            'rocket-fuel',
            'nuclear-fuel',
            'nuclear-fuel-reprocessing',
            'rocket-control-unit',
            'rocket-part',
            'automation-science-pack',
            'logistic-science-pack',
            'chemical-science-pack',
            'military-science-pack',
            'production-science-pack',
            'utility-science-pack',
            'kovarex-enrichment-process'
        ]

        is_legit_module = False
        is_not_full = False
        is_pmodule = False
        is_pmodule_in_list = False

        if module_name in module_list:
            is_legit_module = True
        if len(self.to_add_module_list) < self.machine_obj.module_slots_size:
            is_not_full = True
        if module_name in ['p1', 'p2', 'p3']:
            is_pmodule = True
        if self.item_obj.name in pmodule_list:
            is_pmodule_in_list = True

        if is_legit_module and is_not_full:
            if not is_pmodule:
                return True
            elif is_pmodule and is_pmodule_in_list:
                return True
            else:
                return False
        else:
            return False

    def add_a_module(self, module_name):
        if self.is_able_to_add_a_module(module_name):
            self.to_add_module_list.append(module_name)
            self.update_machine(self.production_machine_name)
        else:
            print('cannot add a module')

    def clear_module(self):
        self.to_add_module_list = []

    def update_machine(self, machine_name):
        if machine_name in self.available_machine_list:
            self.production_machine_name = machine_name
            self.machine_obj = FactorioMachine(self.production_machine_name, self.to_add_module_list, self.mining_research_modifier)
