export async function load({ session }) {
    // You can perform checks here based on the session or fetch data
    const userLoggedIn = session?.user != null;
    
    return {
      userLoggedIn
    };
  }
  