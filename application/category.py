from recipes import Recipe
class Category:
    """ Describes the category model """

    def __init__(self, title):
        self.title = title
        self.recipes = {}

    def add_recipe(self, description):
        """ Adds an Recipe to a category """
        if description:
            if description.strip():
                if not description in self.recipes:
                    self.recipes[description] = Recipe(description)
                    return "Recipe added"
                return "Recipe already exists"
            return "Blank input"
        return "None input"

    def update_description(self, description, new_description):
        """ Updates an Recipe's description in a category """
        if description and new_description:
            if description.strip() and new_description.strip:
                if not new_description == description:
                    if not new_description in self.recipes:
                        if description in self.recipes:
                            self.recipes[new_description] = self.recipes.pop(description)
                            return "Recipe updated"
                        return "Recipe not found"
                    return "New description already in category"
                return "No changes"
            return "Blank input"
        return "None input"

    def update_status(self, description, status):
        """ Updates an Recipe's status in a category """
        if description and status:
            if description.strip() and status.strip():
                if description in self.recipes:
                    if status == "Pending" or status == "Done":
                        if not self.recipes[description].status == status:
                            self.recipes[description].status = status
                            return "Recipe updated"
                        return "No changes"
                    return "Invalid status"
                return "Recipe not found"
            return "Blank input"
        return "None input"

    def delete_recipe(self, description):
        """ Deletes an Recipe from a category """
        if description:
            if description.strip():
                if description in self.recipes:
                    self.recipes.pop(description)
                    return "Recipe deleted"
                return "Recipe not found"
            return "Blank input"
        return "None input"

    def get_recipes_count(self):
        """ Counts recipes in a category """
        return len(self.recipes)

    def get_progress(self):
        """ Gives progress in doing recipes in a category """
        progress = 0
        if self.recipes:
            for recipe in self.recipes.values():
                if recipe.status == 'Done':
                    progress += 1
            return round(100*progress/len(self.recipes))
        return 0
