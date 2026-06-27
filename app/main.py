from fastapi import FastAPI
from app.routers import admin
 
app = FastAPI()
app.include_router(admin.router)


@app.get("/health", status_code=200)
async def health():
    return {"status": "ok"}