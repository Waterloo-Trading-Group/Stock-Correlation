from fastapi import FastAPI
# import ./models/model.stock_corr.py
from models.stock_corr import stock_correlation_model
from scripts.stock_correlation import TickerCorrelation

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "stock correlation"}

@app.get("/stock_correlation/{stock1}/{stock2}", response_model=stock_correlation_model)
async def stock_correlation(stock1: str, stock2: str):
    totalCorr = TickerCorrelation.get_total_correlation(TickerCorrelation, stock1, stock2)
    # generate a new stock_correlation_model object
    return stock_correlation_model(stock1=stock1, stock2=stock2, TotalCorrelation=totalCorr)
    