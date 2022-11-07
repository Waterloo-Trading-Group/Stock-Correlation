#!/usr/bin/env python3
from pydantic import BaseModel

class stock_correlation_model(BaseModel):
    stock1: str
    stock2: str
    TotalCorrelation: float