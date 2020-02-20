#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  whole_batches = []
  for item in recipe.keys():
    if item not in ingredients.keys():
      return 0
  for ingredient, ingredient_recipe in recipe.items():
    batches = ingredients[ingredient] // ingredient_recipe
    # print(batches)
    whole_batches.append(batches)
    # print(whole_batches)
  return(whole_batches) 

# print(recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# ))
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))