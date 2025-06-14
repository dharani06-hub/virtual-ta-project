from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Enable CORS so that browsers can make API requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route (required)
@app.get("/")
def read_root():
    return {"message": "Virtual TA is running!"}

# Request and response models
class Link(BaseModel):
    url: str
    text: str

class Query(BaseModel):
    question: str
    image: Optional[str] = None

class Response(BaseModel):
    answer: str
    links: List[Link]

# POST /api/ endpoint
@app.post("/api/", response_model=Response)
def ask_virtual_ta(query: Query):
    # Dummy static response (replace with logic later)
    return {
        "answer": "Please refer to the Discourse links below for clarification.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "Clarification post about using tokenizers."
            }
        ]
    }
