from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    role: str
    total_rides: int
    active: bool
    hashed_password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True

class Vehicle(BaseModel):
    model: str
    total_rides: int
    current_driver: int
    licence_plate: str
    status: str
    brand: str
    model: str
    year: str
    current_mileage: float
    previous_mileage: float
    vehicle_category: str
    vehicle_location: str
    fuel_type: str
    maintenance_date: datetime
    vehicle_image: str
    notes: str

    class Config:
        orm_mode = True

class Company(BaseModel):
    name: str

    class Config:
        orm_mode = True

class Driver(BaseModel):
    name: str
    hire_date: datetime
    email: str
    birth_date: datetime
    itn: str
    driver_experience: str
    total_trips: int

    class Config:
        orm_mode = True

class DriverDocument(BaseModel):
    document_type: str
    document_number: str
    issued_by: str
    issued_date: datetime
    expiry_date: datetime
    valid: bool

    class Config:
        orm_mode = True

class Trip(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime
    distance: float

    class Config:
        orm_mode = True

class Invite(BaseModel):
    name: str
    phone: str
    email: str
    status: bool
    expires_at: datetime

    class Config:
        orm_mode = True

class VehiclePolicy(BaseModel):
    policy_number: str
    provider: str
    valid_from: str
    valid_until: str
    expired: bool
