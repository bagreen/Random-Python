import argparse

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help='Picks out random recipes to try')
    parser.add_argument('-m', help='Manually pick out recipes to try')
    parser.add_argument('-d', help='Desserts instead!')


class Meal(object):
    ingredients = {}
    instructions = []

    def __init__(self, ingredients, last_eaten):
        self.ingredients = ingredients
        self.last_eaten = last_eaten


# find meals for the week
def meals_for_week():


# make meals from our recipes
def initialize_meals():



def main():
    recipe = Meal({1: "asdf"}, 0)




if __name__ == '__main__':
    main()