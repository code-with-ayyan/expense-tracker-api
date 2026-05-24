from utils.db import base 
from sqlalchemy import Column, DateTime, Integer, Float, String
from typing import Optional
from datetime import datetime



class ExpenseModel(base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    
    amount = Column(Float, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=False) 
    
    created_at = Column(DateTime, default = datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    