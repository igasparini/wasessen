import os
from fastapi import FastAPI
from recipe import Recipe
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

# # Configure CORS to allow requests from your frontend origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Add your frontend URL here
#     allow_credentials=True,
#     allow_methods=["GET", "OPTIONS", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )

@app.get('/api/recipe')
def get_recipe(cooking_time: int, calories: int, keywords: Optional[str] = None):
    recipe = Recipe(cooking_time, calories, keywords)
    return recipe.get_recipe()

### AUTH ###

class SignupRequest(BaseModel):
    email: str
    password: str

@app.post('/api/signup')
async def signup(request: SignupRequest):
    result = supabase.auth.sign_up(request.dict())
    return {"message": "Check your email for the confirmation link"}


@app.post('/api/login')
async def login(email: str, password: str):
    result = supabase.auth.sign_in(email, password)
    if result.error:
        return {"error": str(result.error)}
    return result.data

@app.post('/api/logout')
async def logout():
    result = supabase.auth.sign_out()
    if result.error:
        return {"error": str(result.error)}
    return {"message": "Logged out successfully"}