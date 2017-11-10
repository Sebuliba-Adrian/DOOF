""" Contains the various object models used by the recipe list app """
from category import Catergory
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
