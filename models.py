from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    role = Column(String)
    phone = Column(String)
    total_rides = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))
    active: Column(Boolean, default=True)
    hashed_password = Column(String)

class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    refresh_token = Column(String)

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hire_date = Column(DateTime)
    email = Column(String)
    birth_date = Column(DateTime)
    itn = Column(String)
    driver_experience = Column(String)
    total_trips = Column(Integer)

    document_id = Column(Integer, ForeignKey("driver_documents.id"))
    assigned_vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    document = relationship("DriverDocument")
    vehicle = relationship("Vehicle")
    user = relationship("User")


class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    licence_plate = Column(String)
    status = Column(String)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    current_mileage = Column(Float)
    previous_mileage = Column(Float)
    vehicle_category = Column(String)
    vehicle_location = Column(String)
    fuel_type = Column(String)
    maintenance_date = Column(DateTime)
    vehicle_image = Column(String)
    notes = Column(String)
    total_rides = Column(Integer)

    policy_id = Column(Integer, ForeignKey("vehicle_policies.id"))
    current_driver_id = Column(Integer, ForeignKey("users.id"))
    current_company_id = Column(Integer, ForeignKey("companies.id"))

    policy = relationship("VehiclePolicy")
    current_driver = relationship("User")
    current_company = relationship("Company")

class VehiclePolicy(Base):
    __tablename__ = "vehicle_policies"
    id = Column(Integer, primary_key=True)
    policy_number = Column(String)
    provider = Column(String)
    valid_from = Column(String)
    valid_until = Column(String)
    expired = Column(Boolean)

    # vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    # current_driver = relationship("Vehicle")

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    corporative_email = Column(String)
    corporative_phone = Column(String)
    name = Column(String)
    iban = Column(String)
    vat = Column(String)

class DriverDocument(Base):
    __tablename__ = "driver_documents"
    id = Column(Integer, primary_key=True)
    document_type = Column(String)
    document_number = Column(String)
    issued_by = Column(String)
    issued_date = Column(DateTime)
    expiry_date = Column(DateTime)
    valid = Column(Boolean)

    driver_id = Column(Integer, ForeignKey("drivers.id"))
    driver = relationship("Driver")

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    distance = Column(Float)

    driver_id = Column(Integer, ForeignKey("drivers.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    driver = relationship("Driver")

class Invite(Base):
    __tablename__ = "invites"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    status = Column(String)
    expires_at = Column(DateTime)

    company_id = Column(Integer, ForeignKey("companies.id"))
    driver = relationship("Company")










