from typing import Any
from fastapi import FastAPI,Depends,HTTPException,status
# FastAPI: The main class to create a FastAPI app.
# You use it to define your API and routes.

# Depends: A function used to implement dependency injection.
# It allows FastAPI to call another function/class before executing the endpoint logic.

# HTTPException: Used to return HTTP error responses (like 404, 401, etc.).
# You raise this when something goes wrong (e.g., blog not found).

# status: A helper module providing HTTP status codes like 404_NOT_FOUND, 200_OK, etc.


# below are the sample dictionary examples
blogs={
    "1" : "FastAPI Prerequisite",
    "2" : "Building APIs with FastAPI",
    "3" : "Background Tasks | Celery x FastAPI",
}

users = {
    "8":"Jamie",
    "9":"Roman",
}

app = FastAPI(title="Dependency Injection")

# def get_blog_or_404(id : str):  #this will be only working for the blogs.
#     blog = blogs.get(id)
#     if not blog:
#         raise HTTPException(detail=f"Blog with {id} does not exist",
#                              status_code=status.HTTP_404_NOT_FOUND)
#     return blog



class GetObjectOr404:
    def __init__(self,model) -> None:
        self.model = model
    def __call__(self, id: str): #__call__ is a special method in Python that allows an instance of a class to be called like a function.
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"Object with {id} does not exist",
                             status_code=status.HTTP_404_NOT_FOUND)
        return obj



blog_dependency = GetObjectOr404(blogs)
# Defines a GET API endpoint at /blog/{id}
# {id} is a path parameter passed to the dependency.
@app.get("/blog/{id}")
# def get_blog(blog_name : str = Depends(get_blog_or_404)):
def get_blog(blog_name : str = Depends(blog_dependency)):
    return blog_name


users_dependency = GetObjectOr404(users)
@app.get("/user/{id}")
def user_blog(user_name : str = Depends(users_dependency)):
    return user_name

#uvicorn 07_dependency_injection:app --reload   :to run this file this could be the best