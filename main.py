from fastapi import FastAPI
from utils.db import base, engine
from expenses.models import ExpenseModel
from expenses.router import routers

base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(routers)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}