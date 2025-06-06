# Virtual TA for Tools in Data Science

This is a FastAPI-based virtual assistant to answer student questions using IITM Discourse and course content.

## Run locally

```bash
uvicorn main:app --reload
```

## API Endpoint

POST `/api/` with JSON:

```json
{
  "question": "Your question here",
  "image": null
}
```