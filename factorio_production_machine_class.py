import data.module_modifier_dict
from factorio_item_class import FactorioItem
from data.recipe_dict import recipe_dict
from data.production_machine_dict import production_machine_dict
from data.production_machine_category_list_dict import production_machine_category_list_dict as pmc_list_dict
from data.module_modifier_dict import module_modifier_dict


# production_time = energy_required/production_speed_rate
# modified_rate = base_rate + base_rate*modifier
# extra_product_rate 는 total_requirements를 감소시킴
# resource_consumption_rate = 100*extra_product_rate/(100*extra_product_rate)+1
# 추가 생산품이 존재하기에 실질적으로 생산 속도 배수에 곱연산이 적용되는 효과가 있음.
# production_speed_rate = production_speed_rate*(1+extra_product_rate)


class FactorioMachine:
    total_modifier: list
    production_speed_rate: float
    power_consumption_rate: float
    extra_product_rate: float

    def __init__(self, factory_name, item_obj: FactorioItem, mining_research_modifier=0):
        self.item_to_produce_obj = item_obj
        self.production_machine_name = factory_name

        # production_machine_dict에서 가져올것
        self.base_production_speed_rate = production_machine_dict[self.production_machine_name]['production_rate']
        self.base_power_consumption_rate = production_machine_dict[self.production_machine_name]['power_consumption']
        self.module_slots_size = production_machine_dict[self.production_machine_name]['module_slots']
        self.mining_research_modifier = mining_research_modifier
        self.added_module_list=[]
        self.resource_consumption_rate = self.get_resource_consumption_rate()





    def is_able_to_add_a_module(self, module_name):
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

        # 4가지 조건 기본값 거짓
        is_legit_module = False
        is_not_full = False
        is_pmodule = False
        is_pmodule_in_list = False

        # 4가지 조건 참거짓
        if module_name in module_list:
            is_legit_module = True
        if len(self.added_module_list) <= self.module_slots_size:
            is_not_full = True
        if module_name in ['p1', 'p2', 'p3']:
            is_pmodule = True
        if self.item_to_produce_obj in pmodule_list:
            is_pmodule_in_list = True

        # return
        if not is_pmodule:
            if is_legit_module == True and is_not_full == True:
                return True
            else:
                return False
        else:
            if is_not_full == True and is_pmodule_in_list == True and is_legit_module == True:
                return True
            else:
                return False

    def add_module(self, module_name):
        if self.is_able_to_add_a_module():
            self.added_module_list.append(module_name)
            self.update_module_modifier()
            print(self.added_module_list)
        else:
            print('cannot add module')

    def clear_module(self):
        self.added_module_list = []

    def update_module_modifier(self):
        # [speed, power, extra_product] 순서
        self.total_modifier = [0, 0, 0]
        for added_module in self.added_module_list:
            for i in range(3):
                self.total_modifier[i - 1] = self.total_modifier[i - 1] + module_modifier_dict[added_module][i - 1]

        if self.production_machine_name in pmc_list_dict['mining-drill'] or self.production_machine_name in pmc_list_dict['crude-oil']:
            self.total_modifier[2] = self.total_modifier[2] + self.mining_research_modifier

        self.production_speed_rate = self.base_production_speed_rate + self.base_production_speed_rate * self.total_modifier[0]
        self.power_consumption_rate = self.base_power_consumption_rate + self.base_power_consumption_rate * self.total_modifier[1]
        self.extra_product_rate = self.total_modifier[2]
        # 추가 생산품을 생산 속도에 반영
        self.production_speed_rate = self.production_speed_rate * (1 + self.extra_product_rate)

    def get_resource_consumption_rate(self):
        self.update_module_modifier()
        self.resource_consumption_rate = 100 * self.extra_product_rate / 100 * self.extra_product_rate + 1
        return self.resource_consumption_rate
