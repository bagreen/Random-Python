from typing import List
import argparse
import decimal
import random

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help='Picks out random recipes to try', action='store_true')
    parser.add_argument('-m', help='Manually pick out recipes to try', action='store_true')
    parser.add_argument('-d', help='Desserts instead!', action='store_true')

    try:
        return vars(parser.parse_args())
    except IOError:
        parser.error('Error')
class Meal(object):
    name = ''
    ingredients = {}
    #instructions = []

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        #self.last_eaten = last_eaten
def format_number(num):
    # taken from Stack Overflow, need to play with it
    try:
        dec = decimal.Decimal(num)
    except:
        return 'bad'
    tup = dec.as_tuple()
    delta = len(tup.digits) + tup.exponent
    digits = ''.join(str(d) for d in tup.digits)
    if delta <= 0:
        zeros = abs(tup.exponent) - len(tup.digits)
        val = '0.' + ('0'*zeros) + digits
    else:
        val = digits[:delta] + ('0'*tup.exponent) + '.' + digits[delta:]
    val = val.rstrip('0')
    if val[-1] == '.':
        val = val[:-1]
    if tup.sign:
        return '-' + val
    return val
def add_sizes_together(original_size, add_size):
    original = original_size.split()
    add = add_size.split()

    print(original)
    print(add)

    if len(original) is 1 and len(add) is 1:
        return str(format_number(float(original[0]) + float(add[0])))

    elif original[1] == add[1]:
        return str(format_number(float(original[0]) + float(add[0]))) + ' ' + original[1]

    # write else as errors come up?
    else:
        print('AHHHHH')
        print('Problem comparing', original_size, 'and', add_size)
        exit()


# find meals for the week
def meals_for_week(meals):
    total_ingredients = {}

    for meal in meals:
        for ingredient in meal.ingredients:
            print(ingredient, meal.ingredients[ingredient])

            if ingredient not in total_ingredients:
                total_ingredients[ingredient] = meal.ingredients[ingredient]

            else:
                original_size = total_ingredients[ingredient]
                add_size = meal.ingredients[ingredient]
                total_ingredients[ingredient] = add_sizes_together(original_size, add_size)


    return total_ingredients


def initialize_desserts():
    desserts: List[Meal] = []

    desserts.append(Meal('Banana Bread', {'sugar': '1 cup', 'banana': '2', 'butter': '.5 cup', 'milk': '.25 cup', 'vanilla extract': '1 tsp', 'egg': '2', 'flour': '2 cup', 'nuts': '.5 cup', 'baking soda': '1 tsp', 'salt': '.5 tsp'}))

    desserts.append(Meal('Chocolate Chip Bar Cookies', {'butter': '1 cup', 'brown sugar': '.75 cup', 'sugar': '.75 cup', 'vanilla extract': '1 tsp', 'egg': '2', 'flour': '2.25 cup', 'baking powder': '1 tsp', 'salt': '.5 tsp', 'chocolate chips': '12 oz'}))

    desserts.append(Meal('Chocolate Raspberry Brownie Cake', {'butter': '.5 cup', 'unsweetened chocolate': '3 oz', 'sugar': '1.33 cup', 'pecans': '.5 cup', 'egg': '2', 'vanilla extract': '1 tsp', 'flour': '.66 cup', 'raspberries': '2.5 cup'}))

    return desserts


# make meals from our recipes
def initialize_meals():
    meals: List[Meal] = []

    meals.append(Meal('Blistered Green Bean and Corn Frittata', {'egg': '8', 'olive oil': '3 tbsp', 'green beans': '8 oz', 'shallot': '.33 cup', 'ear of corn': '1', 'cherry tomatoes': '1 pint', 'red wine vinegar': '2 tbsp', 'parsley': '2 tbsp'}))

    meals.append(Meal('Chicken Taco Casserole', {'cream of mushroom soup': '1 can', 'chicken soup': '1 can', 'evaporated milk': '1 small can', 'onion': '1', 'chopped green chilis with liquid': '1 can', 'chicken': '2 lb', 'taco shells': '30', 'cheddar': '1 lb'}))

    meals.append(Meal('Incredible Chicken', {'chicken': '2 lb', 'brown sugar': '0.33 c'}))

    meals.append(Meal('Just Good Chicken', {'dijon mustard': '1 tbsp', 'paprika': '1 tsp', 'chicken': '2 lb'}))

    meals.append(Meal('Olive Garden Zuppa Toscana', {'olive oil': '1 tbsp', 'sausage': '1 lb', 'garlic': '3 clove', 'onion': '1', 'oregano': '.5 tsp', 'russet potato': '3', 'chicken broth': '6 cup', 'kale': '.5 bunch', 'half and half': '1 cup'}))

    meals.append(Meal('Penne Alla Vodka', {'penne': '16 oz', 'onion': '1', 'butter': '4 tbsp', 'canned tomatoes': '16 oz', 'tomato sauce': '8 oz', 'vodka': '.66 cup', 'cream': '1 cup', 'ham': '.25 lb', 'peas': '1 cup', 'red pepper flakes': '.5 tsp'}))

    meals.append(Meal('Simple Roasted Spaghetti Squash', {'spaghetti squash': '3.25 lb'}))

    meals.append(Meal('Stacked Enchiladas', {'tortilla': '6', 'cheddar': '.5 lb', 'enchilada sauce': '10 oz', 'chicken': '.5 lb', 'sour cream': '1 cup', 'green onion': '.25 cup', 'salt': '.5 tsp', 'cumin': '.25 tsp'}))

    meals.append(Meal('Stir Fry Chicken with Broccoli and Cashews', {'soy sauce': '.25 cup', 'sherry': '1.5 tbsp', 'ginger': '.75 tsp', 'chicken': '1.5 lb', 'broccoli': '1 lb', 'vegetable oil': '7 tbsp', 'green onion': '.5 cup', 'garlic': '1 clove', 'cashews': '1.5 cup'}))

    return meals


def main():
    desserts = initialize_desserts()
    meals = initialize_meals()

    result = meals_for_week(meals)

    

    print()
    print()
    for value in result:
        print(result[value], value)

if __name__ == '__main__':
    main()
