import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

const config = defineConfig({
  plugins: [sveltekit()],
  server: {
    proxy: {
      // Forward all requests from SvelteKit starting with '/api' to your FastAPI server
      '/api': {
        target: 'http://localhost:8000', // The default URL FastAPI runs on
        changeOrigin: true,
        secure: false,
      },
    },
  },
});

export default config;
