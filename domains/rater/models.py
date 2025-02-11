from sqlmodel import SQLModel, Field
from typing import Optional

class Rater(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account_id: int = Field(default=None, nullable=True)
    insured_id: int = Field(default=None, nullable=True)
    product_id: int
    business_unit_code: str
    total_exposure_premium: float = Field(default=None, nullable=True)
    modified_premium: float = Field(default=None, nullable=True)
    total_premium: float = Field(default=None, nullable=True)

class BusinessUnit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str = Field(default=None, nullable=True)