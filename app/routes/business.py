from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import AsyncSessionLocal
from app.models import Business  # SQLAlchemy Model
from app.schemas import Business as BusinessSchema, BusinessCreate, BusinessUpdate  # Pydantic Schemas
from typing import List

router = APIRouter()

# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Create a new business
@router.post("/business", response_model=BusinessSchema, status_code=201)
async def create_business(business: BusinessCreate, db: AsyncSession = Depends(get_db)):
    db_business = Business(**business.dict())  # Use dict() for Pydantic v1, model_dump() for v2
    db.add(db_business)
    await db.commit()
    await db.refresh(db_business)
    return db_business

# Retrieve a business by ID
@router.get("/business/{id}", response_model=BusinessSchema)
async def get_business(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Business).where(Business.id == id))
    business = result.scalars().first()
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

# Update contact info for a business
@router.patch("/business/{id}/contact-info", response_model=BusinessSchema)
async def update_contact_info(id: int, contact_info: dict, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Business).where(Business.id == id))
    business = result.scalars().first()
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    
    for key, value in contact_info.items():
        setattr(business, key, value)
    
    await db.commit()
    await db.refresh(business)
    return business

# Search businesses by name
@router.get("/search/businesses", response_model=List[BusinessSchema])
async def search_businesses(business_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Business).where(Business.business_name.ilike(f"%{business_name}%")))
    return result.scalars().all()

# Filter businesses by category, location, or recruitment batch
@router.get("/businesses/filter", response_model=List[BusinessSchema])
async def filter_businesses(category: str = None, location: str = None, recruitment_batch: str = None, db: AsyncSession = Depends(get_db)):
    query = select(Business)
    if category:
        query = query.where(Business.domain == category)
    if location:
        query = query.where(Business.contact_info.ilike(f"%{location}%"))
    if recruitment_batch:
        query = query.where(Business.recruitment_batch == recruitment_batch)
    
    result = await db.execute(query)
    return result.scalars().all()

# Retrieve all businesses
@router.get("/businesses", response_model=List[BusinessSchema])
async def get_all_businesses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Business))
    return result.scalars().all()

# Delete a business by ID
@router.delete("/business/{id}", status_code=204)
async def delete_business(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Business).where(Business.id == id))
    business = result.scalars().first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    await db.delete(business)
    await db.commit()
    return {"detail": "Business deleted successfully"}

# Update a business by ID
@router.put("/business/{id}", response_model=BusinessSchema)
async def update_business(id: int, business_update: BusinessUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Business).where(Business.id == id))
    business = result.scalars().first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    for key, value in business_update.dict(exclude_unset=True).items():
        setattr(business, key, value)
    
    await db.commit()
    await db.refresh(business)
    return business

# Health check endpoint
@router.get("/healthcheck")
async def health_check():
    return {"status": "ok"}
