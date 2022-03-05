from typing import List
import fastapi
import uvicorn
from app.routes.news import router as home_router
from server import app

server_app = app
app.include_router(home_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', reload=True, debug=True, workers=3)
