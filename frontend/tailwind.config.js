/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'background': '#FFEDE1'
      },
      backgroundImage: {
        'logo-gradient': 'linear-gradient(to top, #FEEEE1, #FFF8EF)'
      }
    },
  },
  plugins: [],
};