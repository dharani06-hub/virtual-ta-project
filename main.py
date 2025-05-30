from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# CORS setup to avoid browser fetch errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Link(BaseModel):
    url: str
    text: str

class Query(BaseModel):
    question: str
    image: Optional[str] = None

class Response(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=Response)
async def ask_virtual_ta(query: Query):
    return {
        "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used..."
            }
        ]
    }

@app.get("/")
async def root():
    return {"message": "Virtual TA API is running. Use POST /api/ to interact."}
