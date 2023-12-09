import axios from 'axios';

const ApiService = {
  async getRecipe({ cooking_time, calories, keywords }) {
    try {
      const response = await axios.get('/api/recipe', {
        params: { cooking_time, calories, keywords },
        timeout: 1000, // Set a timeout of 1 second
      });
      return response.data;
    } catch (error) {
      // Handle the timeout or any other errors here
      console.error('API Request Error:', error);
      return { error: 'An error occurred while fetching data.' };
    }
  }
};

export default ApiService;
