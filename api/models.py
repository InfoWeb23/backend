from pydantic import BaseModel

class UserRegistration(BaseModel):
    name: str
    password: str
    registration: str