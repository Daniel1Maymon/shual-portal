from sqlalchemy import Column, ForeignKey, Integer, String, Text
from app.database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, nullable=False)  # Cannot be null
    owner_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    recruitment_batch = Column(String)
    domain = Column(String)
    description = Column(Text)
    contact_info = Column(Text)
    logo = Column(String)  # URL or path to the logo

# Future Service Table
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('businesses.id'))
    service_name = Column(String)
    description = Column(Text)
    price = Column(Integer)