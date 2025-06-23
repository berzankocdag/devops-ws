from fastapi import FastAPI
from routers import items, users
from db.database import create_tables, engine
from models.user import User  # üstte zaten import etmiş olabilirsin
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from devops-ws FastAPI!"}


@app.on_event("startup")
async def startup():
    await create_tables(engine)

app.include_router(items.router)
