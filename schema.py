from pydantic import BaseModel


class EmployeeIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_active: bool


class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    is_active: bool
