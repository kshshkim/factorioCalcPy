from calculator_base import FactorioCalculatorBase


ddd = FactorioCalculatorBase('processing-unit')
ddd.change_machine_to_specific_block('advanced-circuit', 'assembling-machine-2')
print(ddd.json_out())
