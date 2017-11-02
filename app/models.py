

""" Contains the various object models used by the recipe app """
class User:
    """ Describes the user model """

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.categories = {}

class Recipe(object):

    def __init__(self, title, description):
        self.recipe_title = title
        self.recipe_description = description

    def __repr__(self):
        return '<title {}'.format(self.recipe_title)

class Data(object):
    USERS ={}

 

        
