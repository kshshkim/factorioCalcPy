from data.production_machine_dict import production_machine_dict


class ProductionMachine:
    def __init__(self, name):
        self.name = name
        self.production_rate = production_machine_dict[name]['production_rate']
        self.module_slots = production_machine_dict[name]['module_slots']
        self.power_consumption = production_machine_dict[name]['power_consumption']
        self.added_module_list = []
        # self.cannot_produce_list=[]

    def add_module(self, module_name):
        module_list = ['p1', 'p2', 'p3', 'e1', 'e2', 'e3', 's1', 's2', 's3']
        if module_name in module_list:
            if len(self.added_module_list) <= self.module_slots:
                self.added_module_list.append(module_name)
                self.update_module_effects()

    def update_module_effects(self):
        for module in self.added_module_list:
            pass
        pass

    def clear_module(self):
        self.added_module_list = []

class ProductionModule:
    pass