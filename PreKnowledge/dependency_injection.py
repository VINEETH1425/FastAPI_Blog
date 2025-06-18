from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.testclient import TestClient 
development_db = ["DB for developement"]

def get_db_session():
    return development_db

app = FastAPI()

@app.post("/items")
def add_item(item : str,db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message" : f"item added {item}"}

# in the terminal we can see what are the items which are added to the database.
# http://127.0.0.1:8000/docs  we can try