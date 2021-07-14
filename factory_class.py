from data.production_machine_dict import production_machine_dict
from data.module_modifier_dict import module_modifier_dict
from data.productivity_module_available_list import productivity_module_available_list


class Factory:
    def __init__(self, factory_name: str):
        self.factory_name = factory_name
        self.production_rate = production_machine_dict[self.factory_name]['production_rate']
        self.module_slots = production_machine_dict[self.factory_name]['module_slots']
        self.power_consumption = production_machine_dict[self.factory_name]['power_consumption']
        self.category = production_machine_dict[self.factory_name]['category']
