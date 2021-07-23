from FactorioCalcBase.calculator_base import FactorioCalculatorBase


ddd = FactorioCalculatorBase('processing-unit')
ddd.change_machine_to_specific_block('advanced-circuit', 'assembling-machine-2')
print(ddd.json_out())
# import random
# import time
#
# class SangTae:
#     def __init__(self):
#         self.asdf = [1,2,3,4,5]
#
#
# asdd = SangTae()
#
# it = iter(asdd.asdf)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# time.sleep(10)