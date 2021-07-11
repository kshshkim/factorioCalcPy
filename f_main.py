from factorio_calc_class import FactorioCalc


class Body:
    def __init__(self, main_item_name='advanced-circuit', mining_research_modifier=0):
        self.main_item_name = main_item_name
        self.mining_research_modifier = mining_research_modifier
        self.main_item_calc_obj = FactorioCalc(main_item_name, mining_research_modifier=mining_research_modifier)
        self.ingredient_calc_objs_dict = {}
        self.make_ingredient_calc_objs()
        self.resource_consumption_rate_dict = {}
        self.ref_time = self.main_item_calc_obj.get_production_time()  # 기준시간은 메인 아이템이 하나 만들어지는데 걸리는 시간

    def get_main_item_total_req(self):
        return self.main_item_calc_obj.item_obj.get_total_req_dict(1)

    def make_ingredient_calc_objs(self):
        ref = self.get_main_item_total_req()
        for ingredient in ref.keys():
            self.ingredient_calc_objs_dict[ingredient] = FactorioCalc(ingredient, mining_research_modifier=self.mining_research_modifier)

    def update_resource_consumption_rate_dict(self):
        # 메인 아이템과 재료 아이템 계산기 객체에서 아이템 이름, 재료 소모율 리스트를 가져와서 딕셔너리에 저장
        i_rcr_list = self.main_item_calc_obj.get_item_name_and_resource_consumption_rate_list()
        self.resource_consumption_rate_dict[i_rcr_list[0]] = i_rcr_list[1]
        for calc_obj in self.ingredient_calc_objs_dict.values():
            i_rcr_list = calc_obj.get_item_and_resource_consumption_rate_list()
            self.resource_consumption_rate_dict[i_rcr_list[0]] = i_rcr_list[1]
