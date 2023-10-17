from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import JSONResponse

from schemas import AggregationRequestPolyfill, AggregationRequest
from endpoints import get_aggregate_in_polyfill, get_aggregate_in_radius
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://admin:admin@db/admin"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
db = SessionLocal()


@app.post('/aggregate_in_polyfill')
def aggregate_in_polyfill(request: AggregationRequestPolyfill):
    try:
        result = get_aggregate_in_polyfill(db, request)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Неправильные входные данные")


@app.post('/aggregate_in_radius')
def aggregate_in_radius(request: AggregationRequest):
    try:
        result = get_aggregate_in_radius(db, request)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Неправильные входные данные")
