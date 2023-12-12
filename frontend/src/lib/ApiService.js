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
  },

  async signup({ email, password }) {
    try {
      const response = await axios.post('/api/signup', { email, password });
      return response.data;
    } catch (error) {
      console.error('API Request Error:', error);
      return { error: 'An error occurred while signing up.' };
    }
  },

  async login({ email, password }) {
    try {
      const response = await axios.post('/api/login', { email, password });
      return response.data;
    } catch (error) {
      console.error('API Request Error:', error);
      return { error: 'An error occurred while logging in.' };
    }
  },

  async logout() {
    try {
      const response = await axios.post('/api/logout');
      return response.data;
    } catch (error) {
      console.error('API Request Error:', error);
      return { error: 'An error occurred while logging out.' };
    }
  }
};

export default ApiService;
