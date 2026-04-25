from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Week 8 - Async, Background & Cache Service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)