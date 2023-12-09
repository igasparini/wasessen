import unittest
from backend.recipe import Recipe

class TestRecipe(unittest.TestCase):

    def test_get_recipe(self):
        recipe = Recipe(15, 69, None)
        result = recipe.get_recipe()
        self.assertIsNotNone(result)  # Check if result is not None
        print(result)

if __name__ == '__main__':
    unittest.main()