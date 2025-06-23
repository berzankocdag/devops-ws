from fastapi import FastAPI
from routers import items
from db.database import create_tables, engine
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(items.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello from devops-ws FastAPI!"}

@app.on_event("startup")
async def startup():
    await create_tables(engine)

app.include_router(items.router)
