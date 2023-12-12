<script>
  import { goto, invalidateAll } from '$app/navigation';
  import ApiService from '$lib/ApiService';

  let logoClasses = "h-82 w-82 md:h-96 md:w-96 mx-auto transition duration-150 ease-in-out mb-20";

  function shakeLogo() {
    logoClasses += ' animate-shake';
    setTimeout(() => {
      logoClasses = logoClasses.replace(' animate-shake', '');
    }, 500); // Animation lasts for 500ms
  }

</script>

<main class="flex flex-col items-center justify-center min-h-screen bg-logo-gradient p-4">
  <img src="/logo.png" alt="wasessen logo" class={logoClasses} on:click={shakeLogo} on:keyup={shakeLogo} />

  <div class="-mt-20 space-y-4 max-w-sm w-full">
    <button 
      class="bg-indigo-600 hover:bg-indigo-700 text-white text-lg font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out shadow-md focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 w-full"
      on:click={() => goto('/recipe')}>
      Recipe now!
    </button>

    <button 
      class="bg-green-500 hover:bg-green-600 text-white text-lg font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out shadow-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 w-full"
      on:click={() => { /* Define action for 'Weekly menu' */ }}>
      Weekly menu
    </button>
  </div>

</main>

<style>
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
  }
  
  .animate-shake {
    animation: shake 0.5s ease-in-out;
  }
</style>
