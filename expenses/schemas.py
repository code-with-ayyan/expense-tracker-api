from pydantic import BaseModel, Field
from typing import Optional

class ExpenseSchema(BaseModel):
    title: str = Field(..., min_length=1, description="Title is required")
    
    amount: float = Field(..., gt=0, description="Amount must be greater than 0")
    
    category: str = Field(..., min_length=1, description="Category is required")
    
    description: Optional[str] = Field(None, description="Optional field")
    
    
class ExpenseUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    
