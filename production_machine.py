from data.production_machine_dict import production_machine_dict
from data.module_modifier_dict import module_modifier_dict
import copy

class ProductionMachine:
    def __init__(self, name, what_to_produce):
        self.name = name

        self.base_production_rate =production_machine_dict[name]['production_rate']
        self.base_power_consumption=production_machine_dict[name]['power_consumption']

        self.production_rate = copy.deepcopy(self.base_production_rate)
        self.power_consumption = copy.deepcopy(self.base_power_consumption)

        self.module_slots = production_machine_dict[name]['module_slots']

        self.base_extra_product_rate=0
        self.extra_product_rate=0 # TODO extra_product_rate에 영향을 주는 요소 구현


        self.what_to_produce = what_to_produce
        self.added_module_list = []
        # self.cannot_produce_list=[]

    def is_able_to_add_a_module(self, module_name):
        returnbool = False
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
        if len(self.added_module_list) <= self.module_slots:
            is_not_full = True
        if module_name in ['p1', 'p2', 'p3']:
            is_pmodule = True
        if self.what_to_produce in pmodule_list:
            is_pmodule_in_list = True

        # return
        if is_pmodule == False:
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
            self.update_module_effects()
        else:
            print('cannot add module')

    def update_module_effects(self):
        total_modifier=[0,0,0]
        for added_module in self.added_module_list:
            i=3
            while i!=0:
                total_modifier[i-1]=total_modifier[i-1]+module_modifier_dict[added_module][i-1]
                i=i-1
        # [speed, power, extra_product] 순서
        self.production_rate=self.base_production_rate+self.base_production_rate*total_modifier[0]
        self.power_consumption=self.base_power_consumption+self.base_power_consumption*total_modifier[1]
        self.extra_product_rate=self.base_extra_product_rate+total_modifier[2]

    def clear_module(self):
        self.added_module_list = []
