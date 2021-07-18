from data.binary import recipe_dict


class RecipeClass:
    def __init__(self, recipe_name):
        self.amount = None
        self.name = recipe_name
        self.ingredients = recipe_dict[self.name]['ingredients']
        self.results = recipe_dict[self.name]['results']
        self.energy_required = recipe_dict[self.name]['energy_required']
        self.category = self.get_category()

    def get_category(self):
        category: str
        if recipe_dict[self.name].get('category') is not None:
            category = recipe_dict[self.name]['category']
        else:
            category = 'crafting'
        return category

    def is_name_results_match(self):
        if self.results != '' and self.results.get(self.name) is not None:
            return True
        else:
            return False

    def get_results_count(self):
        if self.is_name_results_match():
            return self.results[self.name]
        elif len(self.results.keys()) == 1:
            return list(self.results.values())[0]
        else:
            return -1
