class production_facility:
    def __init__(self, name, speed, module_slots, power_consumption):
        self.name=name
        self.speed=speed
        self.module_slots=module_slots
        self.power_consumption=power_consumption
        self.cannot_produce_list=[]