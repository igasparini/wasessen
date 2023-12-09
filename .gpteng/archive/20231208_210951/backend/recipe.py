import pandas as pd
import json

class Recipe:
    def __init__(self, time, calories, keywords):
        self.time = time
        self.calories = calories
        self.keywords = keywords

    def get_recipe(self):
        dishes = pd.read_csv('recipes/dishes.csv')
        with open('recipes/ingredient_and_instructions.json') as f:
            ingredients_and_instructions = json.load(f)
        tags = pd.read_csv('recipes/tags.csv')

        # Filter dishes based on time and calories
        filtered_dishes = dishes[(dishes['time'] <= self.time) & (dishes['calories'] <= self.calories)]

        # Filter dishes based on keywords
        if self.keywords:
            filtered_dishes = filtered_dishes[filtered_dishes['name'].str.contains(self.keywords)]

        # Select a random dish from the filtered dishes
        selected_dish = filtered_dishes.sample(1).iloc[0]

        # Get the ingredients and instructions for the selected dish
        selected_dish_ingredients_and_instructions = ingredients_and_instructions[selected_dish['slug']]

        # Get the tags for the selected dish
        selected_dish_tags = tags[tags['dish_id'] == selected_dish['id']]['tag'].tolist()

        # Return the selected dish with its ingredients, instructions, and tags
        return {
            'dish': selected_dish.to_dict(),
            'ingredients_and_instructions': selected_dish_ingredients_and_instructions,
            'tags': selected_dish_tags
        }
