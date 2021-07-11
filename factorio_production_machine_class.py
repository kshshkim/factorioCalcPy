from data.production_machine_dict import production_machine_dict
from data.production_machine_category_list_dict import production_machine_category_list_dict as pmc_list_dict
from data.module_modifier_dict import module_modifier_dict


class FactorioMachine:
    # FactorioCalc 에 전달할 것
    total_modifier: list
    production_speed_rate: float
    power_consumption_rate: float
    extra_product_rate: float
    resource_consumption_rate: float
    total_requirement_modifier: float

    def __init__(self, factory_name: str, to_add_module_list=None, mining_research_modifier=0):
        # FactorioCalc 에서 전달받을 것
        self.production_machine_name = factory_name
        if to_add_module_list is None:
            to_add_module_list = []
        self.added_module_list = to_add_module_list
        self.mining_research_modifier = mining_research_modifier

        # production_machine_dict 에서 가져올것
        self.base_production_speed_rate = production_machine_dict[self.production_machine_name]['production_rate']
        self.base_power_consumption_rate = production_machine_dict[self.production_machine_name]['power_consumption']
        self.module_slots_size = production_machine_dict[self.production_machine_name]['module_slots']

        # 인스턴스 생성시 최종 변동치 계산
        self.calculate_modifiers()

    def calculate_modifiers(self):
        # production_time = energy_required/production_speed_rate
        # modified_rate = base_rate + base_rate*modifier
        # extra_product_rate 는 total_requirements 를 감소시킴
        # resource_consumption_rate = (1/extra_product_rate)/(1/extra_product_rate+1)
        # 추가 생산품이 존재하기에 실질적으로 생산 속도 배수에 곱연산이 적용되는 효과가 있음.
        # production_speed_rate = production_speed_rate*(1+extra_product_rate)

        # [speed, power, extra_product] 순서
        self.total_modifier = [0, 0, 0]
        for added_module in self.added_module_list:
            for i in range(3):
                self.total_modifier[i - 1] = self.total_modifier[i - 1] + module_modifier_dict[added_module][i - 1]

        if self.production_machine_name in pmc_list_dict['mining-drill'] or self.production_machine_name in \
                pmc_list_dict['crude-oil']:
            self.total_modifier[2] = self.total_modifier[2] + production_machine_dict[
                self.production_machine_name] * self.mining_research_modifier

        self.production_speed_rate = self.base_production_speed_rate + self.base_production_speed_rate * self.total_modifier[0]
        self.power_consumption_rate = self.base_power_consumption_rate + self.base_power_consumption_rate * self.total_modifier[1]
        self.extra_product_rate = self.total_modifier[2]
        # 추가 생산품을 생산 속도에 반영 생산속도 배수 곱연산 적용
        self.production_speed_rate = self.production_speed_rate * (1 + self.extra_product_rate)
        self.resource_consumption_rate = 1
        if self.extra_product_rate != 0:
            self.resource_consumption_rate = (1/self.extra_product_rate) / (1/self.extra_product_rate + 1)

    def get_resource_consumption_rate(self):
        return self.resource_consumption_rate
