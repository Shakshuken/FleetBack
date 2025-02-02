from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


# class User(Base):
#     id = Column(
#         UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
#     )
#     full_name = Column(String(255), index=True)
#     email = Column(String(100), unique=True, index=True, nullable=False)
#     phone_number = Column(String(13), unique=True, index=True, nullable=True)
#     hashed_password = Column(String(255), nullable=False)
#     is_active = Column(Boolean(), default=True)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     updated_at = Column(
#         DateTime,
#         default=datetime.datetime.utcnow,
#         onupdate=datetime.datetime.utcnow,
#     )
#
#     account_id = Column(
#         UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=True
#     )
#
#     user_role = relationship("UserRole", back_populates="user", uselist=False)
#     account = relationship("Account", back_populates="users")
