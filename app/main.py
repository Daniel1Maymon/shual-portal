from fastapi import FastAPI
from app.database import engine
from app.routes import business

# Create the FastAPI app
app = FastAPI()

# Include the business routes
app.include_router(business.router)

# Create the database tables
@app.on_event("startup")
async def startup():
    import app.models
    async with engine.begin() as conn:
        await conn.run_sync(app.models.Base.metadata.create_all)