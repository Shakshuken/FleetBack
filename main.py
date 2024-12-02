import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Response
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy import event, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import User, Token, DriverDocument
from sqlalchemy.ext.declarative import declarative_base
from datetime import timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_token, authenticate_user, RoleChecker, get_current_active_user, validate_refresh_token
from sqlalchemyseeder import ResolvingSeeder

from models import User
from models import Company
from models import Vehicle

from schema import User as SchemaUser
from schema import Company as SchemaCompany
from schema import Vehicle as SchemaVehicle

load_dotenv(".env")

# event.listen(User.__table__, 'after_create', initialize_table)

app = FastAPI()

Base = declarative_base()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

engine = create_engine(os.environ["DATABASE_URL"])

# seeding database
# @app.on_event("startup")
# def seed():
#     print('11111111111111111111111111111111111111111')
#     connection = engine.connect()
#     session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
#     seeder = ResolvingSeeder(session)
#     new_entities = seeder.load_entities_from_json_file("seed.json")
#     # session.commit()
#     connection.close()

connection = engine.connect()
session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))

if  engine.dialect.has_table(connection, 'users') and not session.query(User).first():
    print('db is empty 111111111')
    seeder = ResolvingSeeder(session)
    new_entities = seeder.load_entities_from_json_file("seed.json")

connection.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create-user", response_model = SchemaUser)
def create_user(user: SchemaUser):
    db_user = User(
        username=user.username, hashed_password=user.password, email=user.email, role=user.role
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


@app.get("/users")
def get_users():
    users = db.session.query(User).all()

    return users


@app.post("/create-company", response_model = SchemaCompany)
def create_company(company: SchemaCompany):
    db_company = Company(
        name = company.name
    )
    db.session.add(db_company)
    db.session.commit()
    return db_company


@app.get("/companies")
def get_companies():
    companies = db.session.query(Company).all()

    return companies


@app.get("/vehicles")
def get_vehicles():
    vehicles = db.session.query(Vehicle).all()

    return vehicles

@app.get("/drivers")
def get_drivers():
    drivers = db.session.query(Driver).all()

    return drivers

@app.get("/drivers-document/{driver_id}")
def get_drivers_document(driver_id):
    drivers_document = db.session.query(DriverDocument).filter(DriverDocument.driver_id == driver_id).all()

    return drivers_document


#
# @app.post("/token", response_model = None)
# async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Response:
#     user = authenticate_user(db.session.query(User).all(), form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
#
#     access_token = create_token(data={"sub": user.username, "role": user.role}, expires_delta=access_token_expires)
#     refresh_token = create_token(data={"sub": user.username, "role": user.role}, expires_delta=refresh_token_expires)
#
#     db_token = Token(
#         access_token=access_token,
#         refresh_token=refresh_token
#     )
#
#     db.session.add(db_token)
#
#     return JSONResponse(content={"access_token": access_token, "refresh_token": refresh_token})

            # (access_token=access_token, refresh_token=refresh_token))


# @app.post("/refresh")
# async def refresh_access_token(token_data: Annotated[tuple[User, str], Depends(validate_refresh_token)]):
#     user, token = token_data
#     access_token = create_token(data={"sub": user.username, "role": user.role}, expires_delta=access_token_expires)
#     refresh_token = create_token(data={"sub": user.username, "role": user.role}, expires_delta=refresh_token_expires)
#
#     refresh_tokens.remove(token)
#     refresh_tokens.append(refresh_token)
#     return Token(access_token=access_token, refresh_token=refresh_token)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
