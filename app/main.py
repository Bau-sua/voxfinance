import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends
from sqlalchemy import select
from app.core.database import engine, get_db

app = FastAPI(title="VoxFinance", description="Finance analysis API")

@app.get("/")
async def root():
    return {"message": "VoxFinance API ready with DB persistence setup"}

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    # Test engine
    async with engine.connect() as conn:
        await conn.execute(select(1))
    # Test session
    result = await db.execute(select(1))
    return {"status": "healthy", "engine": "ok", "session": "ok"}