import pandas as pd
import json
from random import choice
import os

class Recipe:
    def __init__(self, cooking_time, calories, keywords):
        self.cooking_time = cooking_time
        self.calories = calories
        self.keywords = keywords

    def get_recipe(self):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dishes_path = os.path.join(base_dir, 'recipes', 'dishes.csv')
            ingredients_and_instructions_path = os.path.join(base_dir, 'recipes', 'ingredient_and_instructions.json')
            tags_path = os.path.join(base_dir, 'recipes', 'tags.csv')

            dishes = pd.read_csv(dishes_path)
            with open(ingredients_and_instructions_path) as f:
                ingredients_and_instructions = json.load(f)
            tags = pd.read_csv(tags_path)
            
            # Filter dishes based on cooking_time and calories
            filtered_dishes = dishes[(dishes['total_time'] <= self.cooking_time) & (dishes['calories'] <= self.calories)]

            # Filter dishes based on keywords if they exist
            if self.keywords:
                filtered_dishes = filtered_dishes[filtered_dishes['keywords'].str.contains(self.keywords, na=False)]

            if filtered_dishes.empty:
                return {'error': 'No dishes found matching the criteria.'}

            # Select a random dish from the filtered dishes
            selected_dish = filtered_dishes.sample(1).iloc[0]

            # Get the ingredients and instructions for the selected dish
            dish_slug = selected_dish['slug']
            selected_dish_ingredients_and_instructions = ingredients_and_instructions.get(dish_slug, {})

            # Replace nan with None and convert to dictionary for JSON serialization
            selected_dish_dict = selected_dish.where(pd.notna(selected_dish), None).to_dict()

            # Return the selected dish with its ingredients and instructions
            return {
                'dish': selected_dish_dict,
                'ingredients_and_instructions': selected_dish_ingredients_and_instructions
            }
        except Exception as e:
            # In production, you would want to log the exception to a file or monitoring system
            print(e)
            return {'error': 'An error occurred while processing the recipes.'}
