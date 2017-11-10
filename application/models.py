""" Contains the various object models used by the recipe list app """
class User:
    """ Describes the user model """

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.categories = {}

    def add_category(self, category_title):
        """ Adds a new category to the user's categories """
        if category_title:
            if category_title.strip():
                if len(category_title) > 9 and len(category_title) < 61:
                    if not category_title in self.categories:
                        self.categories[category_title] = Category(category_title)
                        return "Category added"
                    return "A category with this name already exists"
                return "Category name should than 2 characters"
            return "Blank input"
        return "None input"

    def update_category(self, title, new_title):
        """ Adds a new category to the user's categories """
        if title and new_title:
            if title.strip() and new_title.strip():
                if not title == new_title:
                    if title in self.categories:
                        if not new_title in self.categories:
                            if len(new_title) > 9 and len(new_title) < 61:
                                self.categories[new_title] = self.categories.pop(title)
                                return "Category updated"
                            return (
                                "Category name should than 2 characters")
                        return "No change, new name already in category"
                    return "Category not found"
                return "No change, same name"
            return "Blank input"
        return "None input"

    def delete_category(self, category_title):
        """ Deletes a category whose name is provided from a user's categories """
        if category_title:
            if category_title.strip():
                if category_title in self.categories:
                    self.categories.pop(category_title)
                    return "Category deleted"
                return "Category not found"
            return "Blank input"
        return "None input"

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

class Recipe:
    """ Describes the recipe model """

    def __init__(self, description):
        self.description = description
        self.status = "Pending"
