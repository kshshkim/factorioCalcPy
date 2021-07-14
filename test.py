from dependency_tree import RecipeDependency
from oil_processing import FactorioOilNeedToRecipe

asdf = RecipeDependency(recipe_name='processing-unit')

print(asdf.get_total_recipe_req_dict())
print(asdf.total_needed_item())

