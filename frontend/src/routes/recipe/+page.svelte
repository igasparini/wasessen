<script>
  import ApiService from '$lib/ApiService';
  import { writable } from 'svelte/store';
  import { goto } from '$app/navigation';

  let cooking_time = '';
  let calories = '';
  let keywords = '';
  let recipe = null;
  let showForm = writable(true);

  const submit = async () => {
    recipe = await ApiService.getRecipe({
      cooking_time: parseInt(cooking_time) || 0,
      calories: parseInt(calories) || 0,
      keywords: keywords || null
    });
    showForm.set(false);
  };

  const fetchAnotherRecipe = async () => {
    recipe = await ApiService.getRecipe({
      cooking_time: parseInt(cooking_time) || 0,
      calories: parseInt(calories) || 0,
      keywords: keywords || null
    });
  };

  const changeParameters = () => {
    showForm.set(true);
  };

</script>

<main class="flex flex-col items-center justify-center min-h-screen bg-logo-gradient p-4">
  {#if $showForm}
    <div class="max-w-md mx-auto p-4 shadow-lg bg-white">
      <h2 class="font-playful text-3xl text-blue-500 text-center mb-4">What are your preferences?</h2>
      <form on:submit|preventDefault={submit}>

        <div class="mb-4">
          <label for="cooking_time" class="block text-gray-700 text-sm font-bold mb-2">Cooking Time:</label>
          <input id="cooking_time" bind:value={cooking_time} type="number" min="0" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>

        <div class="mb-4">
          <label for="calories" class="block text-gray-700 text-sm font-bold mb-2">Calories:</label>
          <input id="calories" bind:value={calories} type="number" min="0" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>

        <div class="mb-6">
          <label for="keywords" class="block text-gray-700 text-sm font-bold mb-2">Keywords:</label>
          <input id="keywords" bind:value={keywords} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" />
        </div>

        <div class="flex items-center justify-between">
          <button type="submit" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Submit
          </button>
        </div>
        
      </form>
    </div>
  {/if}

  {#if recipe && !$showForm}  
  <div class="max-w-md mx-auto p-4">
    <h2 class="font-playful text-3xl text-blue-500">{recipe.dish.name}</h2>
    <img class="w-full h-auto my-4" src={recipe.dish.thumbnail_url} alt={recipe.dish.name} />
    
    <!-- Nutrition Table -->
    <table class="w-full table-auto border-collapse border border-gray-200 my-4">
      <tr>
        <th class="border border-gray-300 bg-white p-2">Calories</th>
        <td class="border border-gray-300 p-2">{recipe.dish.calories}</td>
      </tr>
      <tr>
        <th class="border border-gray-300 bg-white p-2">Carbohydrates (g)</th>
        <td class="border border-gray-300 p-2">{recipe.dish.carbohydrates}</td>
      </tr>
      <tr>
        <th class="border border-gray-300 bg-white p-2">Fat (g)</th>
        <td class="border border-gray-300 p-2">{recipe.dish.fat}</td>
      </tr>
      <tr>
        <th class="border border-gray-300 bg-white p-2">Fiber (g)</th>
        <td class="border border-gray-300 p-2">{recipe.dish.fiber}</td>
      </tr>
      <tr>
        <th class="border border-gray-300 bg-white p-2">Protein (g)</th>
        <td class="border border-gray-300 p-2">{recipe.dish.protein}</td>
      </tr>
      <tr>
        <th class="border border-gray-300 bg-white p-2">Sugar (g)</th>
        <td class="border border-gray-300 p-2">{recipe.dish.sugar}</td>
      </tr>
    </table>

    <!-- Ingredients and Instructions -->
    {#if recipe.ingredients_and_instructions?.ingredient_sections}
      <div class="my-4">
        <h3 class="text-xl font-semibold">Ingredients</h3>
        {#each recipe.ingredients_and_instructions.ingredient_sections as section}
          <h4 class="font-medium text-lg">{section.name}</h4>
          <ul class="list-disc list-inside">
            {#each section.ingredients as ingredient}
              <li>{ingredient.name} - {ingredient.primary_unit.quantity} {ingredient.primary_unit.display}</li>
            {/each}
          </ul>
        {/each}
      </div>
    {/if}
    {#if recipe.ingredients_and_instructions?.instructions}
      <div class="my-4">
        <h3 class="text-xl font-semibold">Instructions</h3>
        <ol class="list-decimal list-inside">
          {#each recipe.ingredients_and_instructions.instructions as instruction}
            <li>{instruction.display_text}</li>
          {/each}
        </ol>
      </div>
    {/if}
    <!-- Video player -->
    {#if recipe.video_url}
      <div class="my-4">
        <!-- svelte-ignore a11y-media-has-caption -->
        <video 
          class="w-full" 
          controls
          height="240">
          <source src={recipe.video_url} type="video/mp4">
        </video>
      </div>
    {/if}

    <!-- Buttons -->
    <div class="flex justify-center space-x-2 mb-4">
      <button 
        class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
        on:click={fetchAnotherRecipe}>
        Another recipe!
      </button>
  
      <button 
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        on:click={changeParameters}>
        Change parameters
      </button>
    </div>

  </div>
{/if}
</main>
