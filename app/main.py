from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db import get_db

app = FastAPI()

@app.get("/db-info")
def db_info(db: Session = Depends(get_db)):
    # 1) Info del servidor
    version = db.execute(text("select version()")).scalar()

    # 2) Crear tabla de prueba si no existe
    db.execute(text("""
        create table if not exists _healthcheck (
            id serial primary key,
            created_at timestamptz not null default now()
        )
    """))

    # 3) Insertar un registro
    db.execute(text("insert into _healthcheck default values"))
    db.commit()

    # 4) Contar registros
    count = db.execute(text("select count(*) from _healthcheck")).scalar()

    return {"postgres_version": version, "healthcheck_rows": count}