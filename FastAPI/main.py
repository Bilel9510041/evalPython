from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel
import os

app = FastAPI()

# Lire le jeton API depuis la variable d'environnement
API_TOKEN = os.getenv("GROQ_API_TOKEN")

class ChatRequest(BaseModel):
    prompt: str

@app.get("/status")
async def status(api_key: str = Header(...)):
    if api_key != API_TOKEN:
        raise HTTPException(status_code=403, detail="Jeton API invalide")
    return {"status": "Application fonctionne correctement avec le jeton API"}

@app.post("/chat")
async def chat(prompt: str = Query(None), body: ChatRequest = None):
    # Si le paramètre de requête 'prompt' est fourni, utiliser ce prompt
    if prompt:
        return {"response": f"You asked: {prompt}"}
    # Si le corps JSON est fourni, utiliser ce prompt
    elif body:
        return {"response": f"You asked: {body.prompt}"}
    else:
        raise HTTPException(status_code=400, detail="Field 'prompt' is required either in query or in body")
