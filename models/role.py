from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Role(Base):
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    name = Column(String(100), index=True)
    description = Column(Text)