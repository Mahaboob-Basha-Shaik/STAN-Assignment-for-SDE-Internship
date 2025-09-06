from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.llm import generate_response

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.get("/")
async def root():
    return {"message": "Chatbot API is running."}

@app.post("/chat")
async def chat(request: ChatRequest):
    user_id = request.user_id
    user_message = request.message

    if not user_id or not user_message:
        return {"error": "user_id and message are required."}

    bot_reply = generate_response(user_id, user_message)
    return {"reply": bot_reply}

@app.get("/app", response_class=HTMLResponse)
async def serve_app():
    with open("frontend/index.html") as f:
        return f.read()
