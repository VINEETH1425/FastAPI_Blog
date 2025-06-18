from pydantic import BaseModel,Field
from typing import Optional,List
from enum import Enum
from datetime import datetime

class Language(str,Enum):
    PY = "python"
    JAVA = "java"
    GO ="go"

class Comment(BaseModel):
    text : Optional[str]=None

class Blog(BaseModel):
    title : str = Field(max_length=10) # there will be so many options in the Field like min_length,max_length
    description : Optional[str]=None # here we are giving the default description value as None
    is_active : bool
    language : Language = Language.JAVA # here we are default value of the language as java
    # created_at : datetime = datetime.now() # if we write like this then we cant make the difference between time created
    # to resolve to show the second object is created at the 5 sec later, then we have to use the Field.
    created_at : datetime = Field(default_factory=datetime.now) # by using this we can get 5 sec later one more object is created.

    comments : Optional[List[Comment]]

first_blog = Blog(title="My title",is_active=True,comments=[{"text":"my first commit"}])
print(first_blog)

import time 
time.sleep(5)

second_blog = Blog(title="My title",is_active=True,comments=[{"text":"my second commit"}])
print(second_blog)