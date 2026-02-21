from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AliosurERP Backend OK"}

@app.get("/db-ping")
def db_ping():
    return {"db": "ok"}

@app.get("/__routes")
def routes():
    return [f"{r.methods} {r.path}" for r in app.router.routes]