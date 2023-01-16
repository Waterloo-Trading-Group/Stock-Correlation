#!/usr/bin/env python3
from pydantic import BaseModel

class total_stock_correlation_model(BaseModel):
    Kendall: float
    Pearson: float
    Spearman: float