from fastapi import FastAPI
from .recipe import Recipe

app = FastAPI()

@app.get("/recipe")
def get_recipe(time: int, calories: int, keywords: str):
    recipe = Recipe(time, calories, keywords)
    return recipe.get_recipe()
