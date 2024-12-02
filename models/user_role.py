from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

# class UserRole(Base):
#     __tablename__ = "user_roles"
#     user_id = Column(
#         UUID(as_uuid=True),
#         ForeignKey("users.id"),
#         primary_key=True,
#         nullable=False,
#     )
#     role_id = Column(
#         UUID(as_uuid=True),
#         ForeignKey("roles.id"),
#         primary_key=True,
#         nullable=False,
#     )
#
#     role = relationship("Role")
#     user = relationship("User", back_populates="user_role", uselist=False)
#
#     __table_args__ = (
#         UniqueConstraint("user_id", "role_id", name="unique_user_role"),
#     )