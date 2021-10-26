import sqlalchemy
from fastapi import FastAPI
from database import metadata, DATABASE_URL, database
from models import employees
from schema import Employee, EmployeeIn

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/employees/{employeeId}", response_model=Employee)
async def get_employee(employeeId: int):
    query = employees.select().where(employees.c.id == employeeId)
    result = await database.fetch_all(query)
    return result[0]


@app.post("/employees/", response_model=Employee)
async def add_employee(employee: EmployeeIn):
    query = employees.insert().values(first_name=employee.first_name,
                                      last_name=employee.last_name, email=employee.email, is_active=employee.is_active)
    last_record_id = await database.execute(query)
    return {**employee.dict(), "id": last_record_id}
