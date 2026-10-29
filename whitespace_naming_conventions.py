# By Kami Bigdely
# PEP8 - whitespaces and variable names.

######################
# SAUCE FOR WHITESPACES: https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements
#
# BLANK LINES, think of like padding
# - Surround top-level function and class definitions with two blank lines 
# - Method definitions inside a class are surrounded by a single blank line
#
# SAUCE FOR NAMING: https://peps.python.org/pep-0008/#naming-conventions
#
# NAMING
# - Never use the characters 'l' (lowercase letter L), 'O' (uppercase letter oh), 
# or 'I' (uppercase letter eye) as single character variable names.
# - Class names should normally use the CapWords convention.
# - Variable names and function names should be lowercase, with words separated 
# by underscores as necessary to improve readability.
# - Constants are written in all capital letters with underscores separating words.
# However its usually on the module level (https://peps.python.org/pep-0008/#constants)
#
# NAMING FOR CLASSES
# - Public attributes should have no leading underscores.
# - Always use self for the first argument to instance methods.
# - Always use cls for the first argument to class methods (@classmethod)
#
# NOTE: Conscious decision of despite preferance for module level only, 
# capitalized constants inside class as it looks more readable and understood in teh context
######################

class Pizza:
    def __init__(self, mybread_type, cheese_type, meat_type, pizza_toppings, size):
        self.bread_type = mybread_type
        self.cheese_type = cheese_type
        self.meat_type = meat_type
        self.toppings = pizza_toppings
        self.size = size

    @classmethod
    def create_chicago_pizza (cls, size):
        BREAD = 'deep-dish bread'
        CHEESE = 'mozzarella cheese'
        MEAT_TYPE = 'italian sausage'
        TOPPINGS = ['green bell pepper', 'mushroom', 'chunky tomato sauce', 'onion']
        return cls(BREAD, CHEESE, MEAT_TYPE, TOPPINGS, size)
    
    @classmethod
    def create_california_pizza(cls, meat_type, size):
        BREAD = 'thin crust'
        CHEESE = 'feta cheese'
        TOPPINGS =['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return cls(BREAD, CHEESE, meat_type, TOPPINGS, size)
    
    def print_info(self):
        print('bread type is: ', self.bread_type)
        print('cheese type is: ', self.cheese_type)
        print('meat type is: ', self.meat_type)
        print('Toppings are: ', end = '')
        print(', '.join(map(str, self.toppings)))

    
myPizza = Pizza.create_california_pizza('chicken', 'large')
myPizza.print_info()