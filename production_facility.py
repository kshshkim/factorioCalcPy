from legacy.production_facility_dict import production_facility_dict


class production_facility:
    def __init__(self, name):
        self.name = name
        self.production_rate = production_facility_dict[name]['production_rate']
        self.module_slots = production_facility_dict[name]['module_slots']
        self.power_consumption = production_facility_dict[name]['power_consumption']
        # self.cannot_produce_list=[]

    def get_cannot_produce_list(self):
        furnace_only = []

        pass
