from pydantic import BaseModel
from typing import Optional

class TradeBase(BaseModel):
    trade_date: Optional[str]

class TradeCreate(TradeBase):
    pass

class TradeUpdate(BaseModel):
    trade_date: Optional[str]

class TradeResponse(TradeBase):
    tradeID: int

    class Config:
        orm_mode: True
