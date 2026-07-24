from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from parser import audit_page
from models import URLRequest

app = FastAPI(title="Page Pulse API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Page Pulse API is running!"}


@app.post("/audit")
def audit(request: URLRequest):
    try:
        return audit_page(request.url)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except TimeoutError as e:
        raise HTTPException(status_code=408, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))