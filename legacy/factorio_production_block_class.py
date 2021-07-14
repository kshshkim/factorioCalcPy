from data.production_machine_category_list_dict import production_machine_category_list_dict as pmc_list_dict
from data.production_machine_dict import production_machine_dict
from factorio_production_machine_class import FactorioMachine
from factorio_item_class import FactorioItem
from data.productivity_module_available_list import productivity_module_available_list
from data.module_modifier_dict import module_modifier_dict
from data.recipe_dict import recipe_dict
# TODO FactorioItem make_child 메소드 FactorioGeneralBlock 클래스에 넣기
# TODO 계산기 객체 how_many 인수 적용


class FactorioBlock:
    def __init__(self, item_or_recipe_name, mining_research_modifier=0):
        self.to_add_module_list = []
        self.name = item_or_recipe_name
        self.mining_research_modifier = mining_research_modifier

    def is_able_to_add_a_module(self, module_name: str):
        module_list = list(module_modifier_dict.keys())

        is_legit_module = False
        is_not_full = False
        is_productivity_module = False
        is_pmodule_available = False

        if module_name in module_list:
            is_legit_module = True
        if len(self.to_add_module_list) < self.machine_obj.module_slots_size:
            is_not_full = True
        if module_name in ['p1', 'p2', 'p3']:
            is_productivity_module = True
        if self.name in productivity_module_available_list:
            is_pmodule_available = True

        if is_legit_module and is_not_full:
            if not is_productivity_module:
                return True
            elif is_productivity_module and is_pmodule_available:
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

    def update_machine(self, machine_name=None, module_list=None):
        if machine_name == None:
            machine_name = self.production_machine_name
        if module_list == None:
            module_list = self.to_add_module_list
        else:
            self.to_add_module_list=module_list

            self.production_machine_name = machine_name
            if len(module_list)>production_machine_dict[self.production_machine_name]['module_slots']:
                while len(module_list) == production_machine_dict[self.production_machine_name]['module_slots']:
                    print(module_list)
                    module_list.pop(-1) # 슬롯이 더 적은 경우 마지막 슬롯부터 제거
            del self.machine_obj
            self.machine_obj = FactorioMachine(self.production_machine_name, to_add_module_list=self.to_add_module_list, mining_research_modifier=self.mining_research_modifier)

    def get_machine_resource_consumption_rate(self):
        return self.machine_obj.resource_consumption_rate

    def get_power_consumption(self):
        return self.machine_obj.power_consumption_rate

    def get_item_name_and_resource_consumption_rate_list(self):
        return [self.name, self.get_machine_resource_consumption_rate()]


class FactorioGeneralBlock(FactorioBlock):
    def __init__(self, item_name='advanced-circuit', mining_research_modifier=0, resource_consumption_modifier_dict=None):
        super().__init__(item_name, mining_research_modifier)
        if resource_consumption_modifier_dict is None:
            resource_consumption_modifier_dict = {}
        self.item_name = self.name
        self.resource_consumption_modifier_dict = resource_consumption_modifier_dict
        self.item_obj = FactorioItem(item_name, resource_consumption_modifier_dict)
        # 선택 가능 머신 설정
        self.available_machine_list = self.get_available_machine_list()
        self.production_machine_name = self.available_machine_list[-1]
        self.machine_obj = FactorioMachine(self.production_machine_name, self.to_add_module_list, self.mining_research_modifier)
        self.production_time = self.get_production_time_per_one()

    # 아이템별 가능한 생산머신
    def get_available_machine_list(self):
        item_category = self.item_obj.get_category()
        machine_list = pmc_list_dict[item_category]
        return machine_list

    def get_production_time_per_one(self):
        # self.update_machine()
        # 아이템 1개당 energy_required 계산
        # advanced-oil-processing의 경우
        energy_required_per_one = self.item_obj.energy_required_per_one
        production_speed_rate = self.machine_obj.production_speed_rate
        production_time = energy_required_per_one / production_speed_rate
        return production_time


class FactorioOilBlock(FactorioBlock):
    def __init__(self, recipe_name):
        super().__init__(item_or_recipe_name='advanced-oil-processing')
        self.recipe_name = recipe_name
        if self.recipe_name == 'advanced-oil-processing':
            self.production_machine_name = 'oil_refinery'
        self.machine_obj = FactorioMachine(self.production_machine_name)

    def get_production_time(self):
        energy_required = recipe_dict[self.recipe_name]['energy_required']
        production_speed_rate = self.machine_obj.production_speed_rate
        production_time = energy_required / production_speed_rate
        return production_time

