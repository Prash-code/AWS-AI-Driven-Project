from fastapi import FastAPI
from agent.agent import handle_request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI L1 Automation Running"}

@app.post("/ask")
def ask(query: str):
    response = handle_request(query)
    return {"response": response}
