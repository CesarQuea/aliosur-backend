from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PRUEBA-XYZ-123"}

@app.get("/db-ping")
def db_ping():
    return {"db": "ok"}