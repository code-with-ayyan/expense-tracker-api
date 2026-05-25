from sqlalchemy.orm import Session
from expenses.models import ExpenseModel
from expenses.schemas import ExpenseSchema, ExpenseUpdate
from fastapi import HTTPException



def add_expense(db: Session, body: ExpenseSchema): 
    new_expense = body.model_dump()
    
    expense = ExpenseModel(**new_expense)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return {'message' : "Expense added Successfully",
            'data' : expense}
    

def update_task(db: Session, id: int, body: ExpenseUpdate):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == id).first()
    if not expense :
        raise HTTPException(status_code=404, detail="Expense not found")
    else:
        data = body.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(expense, key, value)
        db.commit()
        db.refresh(expense)
        return {'message' : "Expense updated Successfully",
                'data' : expense}
        
def delete_expense(db: Session, id: int):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == id).first()
    if not expense :
        raise HTTPException(status_code=404, detail="Expense not found")
    else:
        db.delete(expense)
        db.commit()
        return {'message' : "Expense deleted Successfully",
                'data' : expense}
        
def get_expense_by_id(db: Session, id : int):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == id).first()
    if not expense :
        raise HTTPException(status_code=404, detail="Expense not found")
    else:
        return {"message":"Expense fetched successfully",
                "data" : expense}
        
def get_expense(db: Session, 
    search: str | None = None, 
    category: str | None = None, 
    sort: str | None = None, 
    page: int | None = None, 
    limit: int | None = None):
    
    query = db.query(ExpenseModel)

    
    if search:
        query = query.filter(ExpenseModel.title.ilike(f"%{search}%"))
        
    if category :
        query = query.filter(ExpenseModel.category == category)
    
    if sort :
        if sort == "asc":
            query = query.order_by(ExpenseModel.amount.asc())
        elif sort == "desc":
            query = query.order_by(ExpenseModel.amount.desc())
    if page and limit:   
        skip = (page - 1) * limit

        query = query.offset(skip).limit(limit)
    
    expenses = query.all()
    
    if not expenses:
        raise HTTPException(status_code=404, detail= "Expense not found")

    return expenses