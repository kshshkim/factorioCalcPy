from FactorioCalcBase.data.binary import production_machine_category_list_dict, productivity_module_available_list, \
    module_modifier_dict
from FactorioCalcBase.production_machine import ProductionMachine
from FactorioCalcBase.recipe_class import RecipeClass


class ProductionBlock:
    def __init__(self, recipe_name, machine_name=None, module_list=None, mining_research_modifier=None,
                 preferred_machine_list=None):
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
        self.total_modifier = [0, 0, 0]  # speed, power, extra
        self.power_consumption = 0
        self.production_speed = 0
        self.extra_product_rate = 0
        self.production_time_per_recipe = 0
        self.preferred_machine_list = preferred_machine_list

        self.update_machine()

    def get_available_machine_list(self):
        recipe_category = self.recipe_obj.category
        machine_list = production_machine_category_list_dict.get(recipe_category)
        return machine_list

    def is_this_machine_available(self, machine_name):
        if machine_name is None:
            return False
        elif machine_name in self.available_machine_list:
            return True
        else:
            return False

    def set_default_machine(self):
        is_set = False
        if (self.preferred_machine_list is not None) or (self.preferred_machine_list != []):
            for each_preferred_machine in self.preferred_machine_list:
                if each_preferred_machine in self.available_machine_list:
                    self.machine_name = each_preferred_machine
                    is_set = True
        #
        if is_set is False:
            self.machine_name = self.available_machine_list[-1]

    def update_machine(self, machine_name=None):

        if self.is_this_machine_available(machine_name):
            self.machine_name = machine_name
        else:
            self.set_default_machine()

        self.machine_obj = ProductionMachine(self.machine_name)
        self.set_module(self.module_list)  # 초기화 후 모듈 재설정

    def set_module(self, module_code_or_list=None):
        check_list = None

        if module_code_or_list is None:
            check_list = []
        elif type(module_code_or_list) is str:
            check_list = [module_code_or_list]
        elif type(module_code_or_list) is list:
            check_list = module_code_or_list

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

        self.update_and_calculate_at_once()

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

    def update_total_modifier(self):
        module_list = self.module_list
        total_modifier = [0, 0, 0]  # speed, power, extra
        if len(module_list) != 0:
            for module in self.module_list:
                for i in range(3):
                    total_modifier[i] += module_modifier_dict[module][i]
            for i in range(3):
                total_modifier[i] = round(total_modifier[i], 4)
        if (self.mining_research_modifier != 0) and (self.recipe_obj.category in ['mining-drill', 'crude-oil']):
            total_modifier[2] += self.mining_research_modifier
        self.total_modifier = total_modifier

    def calculate_total_modifier(self):
        base_list = [self.machine_obj.base_speed_rate, self.machine_obj.base_power_consumption, 0]
        return_list = [0, 0, 0]  # speed, power, extra
        for i in range(2):
            return_list[i] = base_list[i] + base_list[i] * self.total_modifier[i]

        return_list[2] = 1 + self.total_modifier[2]

        if return_list[2] != 1:
            return_list[0] = return_list[0] * (return_list[2])

        self.production_speed = return_list[0]
        self.power_consumption = return_list[1]
        self.extra_product_rate = return_list[2]
        self.production_time_per_recipe = self.recipe_obj.energy_required / self.production_speed

    def update_and_calculate_at_once(self):
        self.update_total_modifier()
        self.calculate_total_modifier()
