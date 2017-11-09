class Recipe:
    def __init__(self,name):
        self.name=name
        self.description =None
        self.ingredients = [] or None
        self.status='Public' or 'Private'

    def set_status(self,status):
        if status=='Public' or status=='Private':
            self.status=status
            return True
        else:
            return 'Invalid status'


    def get_status(self):
        return self.status

    def set_name(self,name):
        if name is None:
            return 'Name cannot be None'
        elif name=='':
            return 'Name cannot be empty'
        else:
            self.name=name
            return True

    def get_name(self):
        return self.name

class Category:
    def __init__(self,name):
        self.name=name
        self.recipes={}

    def get_recipes(self):
        return self.recipes

    def add_recipe(self,recipe):
        if recipe is None:
            return 'Input cannot be None'
        elif not isinstance(recipe,Recipe):
            return 'Input should be of type Recipe'
        else:
            self.recipes[recipe.name]=recipe
            return True

class User:    
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password
        self.categories={}

    def get_categories(self):
        return self.categories

    def add_category(self,category):
        if category is None:
            return 'Input cannot be None'
        elif not isinstance(category,Category):
            return 'Input must be of type Category'
        else:
            self.categories[category.name]=category
            return True
    