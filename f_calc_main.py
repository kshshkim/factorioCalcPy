from factorio_production_block_class import FactorioProductionBlock
from factorio_item_class import FactorioItem


class FactorioCalcBody:
    def __init__(self, main_item_name='advanced-circuit', mining_research_modifier=0, machine_amount=1):
        self.main_item_name = main_item_name
        self.main_machine_amount = machine_amount

        self.initial_total_req_dict = {}
        self.initial_create_total_req_dict()
        self.total_req_dict = self.initial_total_req_dict

        self.block_objs_dict = {}
        self.initial_create_factorio_production_block_objs_dict()

        self.main_block_obj = self.block_objs_dict[self.main_item_name]

        self.resource_consumption_rate_dict = {}

    def initial_create_total_req_dict(self):
        temp_obj = FactorioItem(self.main_item_name)
        self.initial_total_req_dict = temp_obj.get_total_req_dict()

    def initial_create_factorio_production_block_objs_dict(self):
        temp_total_req_dict = self.initial_total_req_dict
        for key in temp_total_req_dict.keys():
            self.block_objs_dict[key] = FactorioProductionBlock(key, mining_research_modifier=0) # 추후 mining_research_modifier 반영 수정 필요

    # update 들

    def update_total_req_dict(self):
        # 생산성 모듈 등으로 특정 아이템의 resource_consumption_rate 가 변동될 경우 필요
        # total_req_dict 에 resource_consumption_rate_dict 가 반영됨.
        temp_obj = FactorioItem(self.main_item_name, self.resource_consumption_rate_dict)
        self.total_req_dict = temp_obj.get_total_req_dict()
        if self.main_machine_amount != 1:
            for key in self.total_req_dict.keys():
                self.total_req_dict[key]=self.total_req_dict[key]*self.main_machine_amount

    def update_resource_consumption_rate_dict(self):
        for block_obj in self.block_objs_dict.values():
            temp_list = block_obj.get_item_name_and_resource_consumption_rate_list()
            self.resource_consumption_rate_dict[temp_list[0]] = temp_list[1] # 0은 이름, 1은 자원소모 배율
        self.update_total_req_dict()

    def get_total_calculated_dict(self):  # 최종 출력
        self.update_resource_consumption_rate_dict()
        new_dict={}
        for block_obj in self.block_objs_dict.values():
            power_consumption = block_obj.get_power_consumption()*self.get_how_many_machine_needed(block_obj)
            amount_needed = self.total_req_dict[block_obj.item_name]
            production_machine_amount = self.get_how_many_machine_needed(block_obj)
            amount_per_minute = production_machine_amount*60/block_obj.get_production_time_per_one()
            if block_obj.item_name not in ['petroleum-gas', 'light-oil', 'heavy-oil', 'crude-oil', 'solid-fuel']:
                new_dict[block_obj.item_name]={
                    'item_name': block_obj.item_name,
                    'amount_needed': round(amount_needed, 2),
                    'production_machine': block_obj.production_machine_name,
                    'added_modules': block_obj.to_add_module_list,
                    'production_machine_amount': production_machine_amount,
                    'amount_per_1_minute': amount_per_minute,
                    'power_consumption(kw)': power_consumption,
                    'power_consumption(mw)': round(power_consumption/1000, 2),
                    'power_consumption(gw)': round(power_consumption/1000000, 2)
                }
            else:
                new_dict[block_obj.item_name]={
                    'item_name': block_obj.item_name,
                    'amount_needed': round(amount_needed, 2),

                }
        return new_dict

    def get_how_many_machine_needed(self, ingredient_block_obj: FactorioProductionBlock):
        # 기준 시간은 메인 아이템이 하나 만들어지는데 걸리는 시간, 모든 재료*요구량은 기준 시간 내에 생산이 되어야함. 기준 시간 내에 생산 가능한 공장의 갯수를 구해야함.
        # 공장 필요량 = 생산해야할 수량 * 1개 생산에 걸리는 시간 / 기준시간
        amount_to_produce = self.total_req_dict[ingredient_block_obj.item_name]
        production_time_per_one = ingredient_block_obj.get_production_time_per_one()
        ref_time = self.block_objs_dict[self.main_item_name].get_production_time_per_one()
        amount_machine_needed = amount_to_produce * production_time_per_one / ref_time
        return round(amount_machine_needed,2)

