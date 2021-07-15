from production_block import ProductionBlock
from production_machine import ProductionMachine
from dependency_tracker import DependencyDictMerged
from recipe_class import RecipeClass


class FactorioCalculator:
    def __init__(self, recipe_name='advanced-circuit', amount=1, mining_research_modifier=0):
        self.recipe_name = recipe_name
        self.recipe_obj = RecipeClass(self.recipe_name)
        self.amount = amount
        self.mining_research_modifier =  mining_research_modifier
        self.main_block_obj = ProductionBlock(self.recipe_name, self.mining_research_modifier)
        self.block_obj_dict = {}

    def make_initial_block_objs(self):
        new_obj = DependencyDictMerged(self.recipe_name, self.amount)