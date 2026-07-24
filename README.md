# 🔎 Page Pulse

Page Pulse is a web application that audits any public webpage and provides a quick SEO and content summary.

It accepts a URL, fetches the webpage, analyzes its HTML, and returns useful metrics such as HTTP status, response time, page title, meta description, H1 count, images missing alt text, and approximate word count.

---

## Features

- URL validation
- HTTP status detection
- Response time measurement
- Page title extraction
- Meta description extraction
- H1 tag count
- Images missing alt text
- Approximate word count
- Error handling for:
  - Invalid URLs
  - Timeouts
  - Non-HTML responses

---

## Tech Stack

### Frontend

- React
- Vite
- Tailwind CSS

### Backend

- FastAPI
- Requests
- BeautifulSoup4
- Pytest

---

## Project Structure

page-pulse/
│
├── backend/
│ ├── main.py
│ ├── parser.py
│ ├── models.py
│ └── tests/
│
├── frontend/
│
└── README.md

---

## Installation

### Clone Repository

```bash
git clone <YOUR_GITHUB_REPO>
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

(or another available port)

---

## API Contract

### POST /audit

Request

```json
{
  "url": "https://example.com"
}
```

Successful Response

```json
{
  "status": 200,
  "response_time_ms": 145,
  "title": "Example Domain",
  "meta_description": "...",
  "h1_count": 1,
  "missing_alt_images": 0,
  "word_count": 125
}
```

Error Response

```json
{
  "detail": "Please enter a valid HTTP or HTTPS URL."
}
```

---

## Design Decisions

### 1. FastAPI

I chose FastAPI because it is lightweight, fast, provides automatic API documentation through Swagger UI, and is well suited for REST APIs.

### 2. BeautifulSoup

BeautifulSoup was used because it can parse imperfect HTML reliably and provides simple methods to extract titles, headings, meta tags, and images.

### 3. Structured Error Handling

The backend validates URLs, detects non-HTML responses, and handles network failures gracefully. This ensures the application returns meaningful error messages instead of crashing.

---

## Testing

The project includes automated tests using Pytest.

Tested scenarios:

- Valid webpage (Happy Path)
- Invalid URL
- Non-HTML response

Run tests

```bash
pytest
```

---

## Future Improvements

If I had more time, I would add:

- Asynchronous page fetching using httpx
- Additional SEO metrics
- Performance scoring
- Export reports as PDF
- Request caching

---

## Live Demo

Frontend:

(Add after deployment)

Backend:

(Add after deployment)

---

## Credit

Built for Digital Heroes Training Task

https://digitalheroesco.com

## AI Usage

AI was used as a development assistant during this project.

### How AI was used
- Understanding the project requirements and planning the implementation.
- Getting guidance on the FastAPI backend and React frontend structure.
- Troubleshooting development issues, including testing, Git, GitHub, Render, and Vercel deployment.
- Reviewing code quality and suggesting improvements.
- Assisting with writing and organizing the README.

### What I completed myself
- Wrote and integrated the application code.
- Implemented the frontend and backend.
- Created and ran the test cases.
- Deployed the backend on Render and the frontend on Vercel.
- Verified the application's functionality and fixed issues during development.

All AI-generated suggestions were reviewed, modified where necessary, and tested before being included in the final project.