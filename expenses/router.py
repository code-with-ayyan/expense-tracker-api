from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db import get_db
from expenses.schemas import ExpenseSchema, ExpenseUpdate
import expenses.controllers as controller

routers = APIRouter()

@routers.post("/expenses")
def add_expense(body: ExpenseSchema, db: Session = Depends(get_db)):
    return controller.add_expense(db, body)

@routers.get("/expenses/{id}")
def get_expense_by_id(id: int, db: Session = Depends(get_db)):
    return controller.get_expense_by_id(db, id)

@routers.patch("/expenses/{id}")
def update_expense(id: int, body: ExpenseUpdate, db: Session = Depends(get_db)):
    return controller.update_task(db, id, body)

@routers.delete("/expenses/{id}")
def delete_expense(id: int, db:Session = Depends(get_db)):
    return controller.delete_expense(db, id)

@routers.get("/expenses")
def get_expense_query(db : Session = Depends(get_db),
    search: str | None = None, 
    category: str | None = None, 
    sort: str | None = None, 
    page: int | None = None, 
    limit: int |None = None):
    
    return controller.get_expense(db, search, category, sort, page, limit)