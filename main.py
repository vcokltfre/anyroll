from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI(docs_url=None)

@app.get("/")
async def get_index():
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.get("/{any}")
async def get_any(any: str):
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
