from pydantic import BaseModel , EmailStr , Field
from typing import Optional,Annotated

class Student (BaseModel):

    name: str = 'mayank'
    age: Optional[int]= None
    email : EmailStr
    cgpa: float = Field(gt = 0, lt=10,default = 5,description='dnasnasj jdsoajdoasj asjdoasjdjsoadj  ojasojdojasodj j aosjdojao joaj oja joj o')


new_student = {'age':'32','email':'dianisaid@gmail.com',}

student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])
