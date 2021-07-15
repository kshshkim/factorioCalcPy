from data.production_machine_dict import production_machine_dict
from data.module_modifier_dict import module_modifier_dict
from data.productivity_module_available_list import productivity_module_available_list


class ProductionMachine:
    def __init__(self, machine_name: str):
        self.machine_name = machine_name
        self.base_speed_rate = production_machine_dict[self.machine_name]['production_rate']
        self.module_slots = production_machine_dict[self.machine_name]['module_slots']
        self.base_power_consumption = production_machine_dict[self.machine_name]['power_consumption']
        self.category = production_machine_dict[self.machine_name]['category']
