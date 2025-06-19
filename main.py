# this is the main entry point for the fastapi.
from fastapi import FastAPI
from core.config import settings

# app = FastAPI(title="Blog",version="0.1.0") this is one way of initializing but we need for dynamic

app= FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.get("/") # when anyone visits the index page then it should go to this page.
def hello():
    return {"msg":"hello FastApi"}

# Now, let's understand what we did, We are creating an instance of FastAPI and initialized it with a title and a project version. Now, we can reference the 'app' as a fastapi class object and use it to create routes.

# @app.get('/') is called a decorator. A decorator is used to provide extra functionality to a function. 
# '/' means that this is the home endpoint. Had it been '/about/' It would mean that whenever someone searches for example.com/about/, run this function.
# get here is called a verb. There are HTTP verbs that determine the functionality allowed for a request. In this case, get means "A user may connect to this home route to retrieve some information."

# More on HTTP verbs:
# GET:  Requests using GET should only retrieve data.

# POST: The POST method is used to submit an entity to the specified resource, e.g. submitting a form.

# PUT: The PUT method is used to update a database table record.

# DELETE: The DELETE method deletes the specified resource.