from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/message", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Simple rule-based logic for now
    msg = request.message.lower()
    if "plan" in msg or "route" in msg:
        return {"response": "I can help you plan a ride! Check out the 'Host Ride' section."}
    elif "safety" in msg:
        return {"response": "Safety first! Always wear a helmet and check your bike before riding."}
    elif "hello" in msg or "hi" in msg:
        return {"response": "Hello rider! How can I assist you today?"}
    else:
        return {"response": "I'm still learning. Try asking about rides or safety!"}
