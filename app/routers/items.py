from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.database import AsyncSessionLocal
from models.item import Item as ItemModel
from schemas.item import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])

def get_session_local():
    yield AsyncSessionLocal()

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_session_local)):
    db_item = ItemModel(name=item.name)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[Item])
async def read_items(db: AsyncSession = Depends(get_session_local)):
    result = await db.execute(select(ItemModel))
    items = result.scalars().all()
    return items
