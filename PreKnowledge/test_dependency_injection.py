from dependency_injection import app, get_db_session
from fastapi.testclient import TestClient  # ✅ Correct import
print(TestClient)

testing_db = ["DB for testing"]

def get_testing_db():
    return testing_db

app.dependency_overrides[get_db_session] = get_testing_db   # the only use of this is to use the testing database instead of normal database

# once comment this code and uvicorn test_dependency_injection:app --reload , this will be giving db for development when commented,
# otherwise db for testing when not commented. So do execute in the uvicorn and see in the terminal.

client = TestClient(app)

def test_item_should_add_to_database():
    response = client.post("/items/?item=sugar",)
    assert response.status_code == 200
    assert response.json() == {"message": "added item sugar"}
