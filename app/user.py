
from app.category import Category
class User(object):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.categories = {}

    
    def add_category(self, category_title):
        if category_title:
            if category_title.strip():
                if len(category_title) > 9 and len(category_title) < 61:
                    if not category_title in self.categories:
                        self.categories[category_title] = Category(
                            category_title)
                        return "category added"
                    return "An category with this name already exists"
                return "category name should be greater than 10 and less than 60 characters"
            return "Blank input"
        return "None input"

