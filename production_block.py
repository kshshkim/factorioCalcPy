from data.production_machine_category_list_dict import production_machine_category_list_dict
from data.productivity_module_available_list import productivity_module_available_list
from data.module_modifier_dict import module_modifier_dict
from production_machine import ProductionMachine
from recipe_class import RecipeClass


class ProductionBlock:
    def __init__(self, recipe_name, machine_name=None, module_list=None, mining_research_modifier=None):
        self.recipe_name = recipe_name
        self.recipe_obj = RecipeClass(self.recipe_name)
        if module_list is None:
            module_list = []
        if mining_research_modifier is None:
            mining_research_modifier = 0
        self.mining_research_modifier = mining_research_modifier
        self.module_list = module_list
        self.machine_name = machine_name
        self.machine_obj = None
        self.available_machine_list = self.get_available_machine_list()
        self.update_machine()
        self.total_modifier = self.get_total_modifier()


    def get_available_machine_list(self):
        recipe_category = self.recipe_obj.category
        machine_list = production_machine_category_list_dict[recipe_category]
        return machine_list

    def update_machine(self):
        if (self.machine_name is None) or (self.machine_name not in self.available_machine_list):
            print(self.available_machine_list)
            self.machine_obj = ProductionMachine(self.available_machine_list[-1])
        else:
            self.machine_obj = ProductionMachine(self.machine_name)
        self.set_module(self.module_list)

    def set_module(self, module_code_or_list=None):
        check_list = None
        if type(module_code_or_list) is str:
            check_list = [module_code_or_list]
        elif type(module_code_or_list) is list:
            check_list = module_code_or_list
        elif module_code_or_list is None:
            check_list = []

        can_add = []

        if check_list is not None:
            for md in check_list:
                if self.can_this_module_be_added(md):
                    can_add.append(md)

        if self.machine_obj.module_slots > 0:
            if len(can_add) <= self.machine_obj.module_slots:
                self.module_list = can_add
            else:
                self.module_list = can_add[:self.machine_obj.module_slots]

        self.get_total_modifier()
        # self.module_list

    def can_this_module_be_added(self, module_code: str):
        is_legit = False
        is_p = False
        is_recipe_in_p_list = False

        if module_code in module_modifier_dict.keys():
            is_legit = True

        if module_code[0] == 'p':
            is_p = True

        if self.recipe_name in productivity_module_available_list:
            is_recipe_in_p_list = True

        if is_legit is True and is_p is False:
            return True
        elif is_legit and is_p and is_recipe_in_p_list:
            return True

    def get_total_modifier(self):
        module_list = self.module_list
        total_modifier = [0, 0, 0]
        if len(module_list) != 0:
            for module in self.module_list:
                for i in range(3):
                    total_modifier[i] += module_modifier_dict[module][i]
            for i in range(3):
                total_modifier[i] = round(total_modifier[i], 4)
        if self.mining_research_modifier != 0 and self.recipe_obj.category == 'mining-drill':
            total_modifier[2] += self.mining_research_modifier
        self.total_modifier = total_modifier
        self.get_modifiers_calculated()
        return total_modifier

    def get_modifiers_calculated(self):
        base_list = [self.machine_obj.base_speed_rate, self.machine_obj.base_power_consumption, 0]
        return_list = [0, 0, 0]
        for i in range(2):
            return_list[i] = base_list[i] + base_list[i] * self.total_modifier[i]
            return_list[2] = self.total_modifier[2]

            if return_list[2] != 0:
                return_list[0] = return_list[0] * (return_list[2] + 1)

