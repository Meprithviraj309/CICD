from app import app

def text_home_page():
    tester=app.test_client()
    responce= tester.get("/")


    assert responce.status_code == 200
    assert b"welcome to flask" in responce.data