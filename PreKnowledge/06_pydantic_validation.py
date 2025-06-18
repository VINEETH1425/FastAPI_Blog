from pydantic import BaseModel,validator,root_validator

class CreateUser(BaseModel):
    email : str
    password : str
    confirm_password : str

    @validator("email") # this will be validating only single value
    def validate_email(cls,value):
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value
    
    # if we want to validate more than value then we have to user root_validator
    @root_validator()
    def validate_password(cls,values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password!=confirm_password :
            raise ValueError("The two passwords should match")
        return values
    

CreateUser(email="ping@fastapitutorial.com",password="123",confirm_password="123")
