from pydantic import Field
from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):

    name: str
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default = 5, description = "A decimal value respresenting cgpa of student")

new_student = {"name" : "Mayank", "age": 21, "email" :"abc@gmail.com", "cgpa": 4}

student = Student(**new_student)

student_json = student.model_dump_json()
print(student_json)