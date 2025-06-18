class Pydantic:
    def is_valid(self, text):
        if "admin" in text:
            return False
        return True

class Starlette:
    def is_valid(self, text):
        return True

class FastAPI(Pydantic, Starlette): # here first inheritance is done for the Pydantic
    pass

f = FastAPI()
print(f.is_valid("admin tried to signin"))

'''
Explanation:
This demonstrates multiple inheritance.

FastAPI inherits from both Pydantic and Starlette.

When f.is_valid() is called, Python uses Method Resolution Order (MRO):

Since Pydantic comes first in class FastAPI(Pydantic, Starlette), the is_valid method from Pydantic is used.

So, the check if "admin" in text evaluates to True → returns False.
'''