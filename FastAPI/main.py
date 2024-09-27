from fastapi import FastAPI, Header, HTTPException
import os

app = FastAPI()

# Lire le jeton API depuis la variable d'environnement
API_TOKEN = os.getenv("GROQ_API_TOKEN")

@app.get("/status")
async def status(api_key: str = Header(...)):
    if api_key != API_TOKEN:
        raise HTTPException(status_code=403, detail="Jeton API invalide")
    return {"status": "Application fonctionne correctement avec le jeton API"}

@app.post("/chat")
async def chat(prompt: str):
    return {"response": f"You asked: {prompt}"}
