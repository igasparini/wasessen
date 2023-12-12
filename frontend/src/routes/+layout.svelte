<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import ApiService from '$lib/ApiService';
  import "../app.css";

  export let data;

  let showForm = false;
  let email = '';
  let password = '';
  let showSuccessMessage = false;
  let errorMessage = '';

  // Toggle form visibility
  function toggleForm(event) {
    event.stopPropagation(); // Stop the event from propagating to the window
    showForm = !showForm;
}

  function clickOutside(node) {
  const handleClick = event => {
    if (!node.contains(event.target)) {
      showForm = false; // Close the form when the click is outside
    }
  };

  window.addEventListener('click', handleClick);

  return {
    destroy() {
      window.removeEventListener('click', handleClick);
    }
  };
}

  async function handleSignup() {
    const response = await ApiService.signup({ email, password });
    if (response.error) {
      errorMessage = response.error;
    } else {
      showSuccessMessage = true;
      setTimeout(() => {
        showSuccessMessage = false;
        showForm = false;
        email = '';
        password = '';
      }, 2000); // Message closes after 2 sec
    }
  }

  async function handleLogin() {
    const response = await ApiService.login({ email, password });
    if (response.error) {
      errorMessage = response.error; // Display error message to user
    } else {
      goto('/some-success-page'); // Navigate to a success page
    }
  }

</script>

<nav class="bg-logo-gradient py-3 px-4 shadow-md">
  <div class="flex justify-between items-center max-w-6xl mx-auto">
    <img src="/logo.png" alt="wasessen logo" class="h-12 w-auto cursor-pointer" on:click={() => goto('/')}>

    {#if data.userLoggedIn}
      <button 
        class="bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out shadow focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50"
        on:click={() => goto('/profile')}>
        Profile
      </button>
    {:else}
      <button 
        class="bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out shadow focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50"
        on:click={event => toggleForm(event)}>
        Login/Signup
      </button>
    {/if}
  </div>
</nav>

{#if showForm}
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
    <div class="bg-white py-5 px-10 rounded-lg shadow-md max-w-sm w-full" use:clickOutside>
      <input 
        type="email" 
        bind:value={email} 
        placeholder="Email"
        class="w-full px-4 py-2 rounded-lg border-2 border-gray-300 mb-4 focus:outline-none focus:border-indigo-500 transition duration-300"
      >
      <input 
        type="password" 
        bind:value={password} 
        placeholder="Password"
        class="w-full px-4 py-2 rounded-lg border-2 border-gray-300 mb-4 focus:outline-none focus:border-indigo-500 transition duration-300"
      >

      {#if errorMessage}
        <p class="text-red-500 text-sm mb-3">{errorMessage}</p>
      {/if}

      <button 
        class="bg-purple-500 hover:bg-purple-600 text-white text-lg font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out shadow-md focus:outline-none focus:ring-2 focus:ring-purple-400 focus:ring-opacity-50 w-full mb-3"
        on:click={handleSignup}>
        Sign Up
      </button>
      <button 
        class="bg-teal-500 hover:bg-teal-600 text-white text-lg font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out shadow-md focus:outline-none focus:ring-2 focus:ring-teal-400 focus:ring-opacity-50 w-full"
        on:click={handleLogin}>
        Log In
      </button>
    </div>
  </div>
{/if}

{#if showSuccessMessage}
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
  <div class="bg-logo-gradient text-black text-xl font-bold py-5 px-10 rounded-lg shadow-md">
    Signup successful! Redirecting...
  </div>
</div>
{/if}

<slot />