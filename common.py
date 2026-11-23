from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Murthy"}

@app.get("/home")
def home():
    return {"message": "Hello Narasimha"}