from fastapi import FastAPI
# import ./models/model.stock_corr.py
from models.total_stock_corr import total_stock_correlation_model
from models.monthly_stock_corr import monthly_stock_correlation_model
from scripts.stock_correlation import TickerCorrelation
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
async def root():
    return "Hello World"

@app.get("/stock_correlation/{stock1}/{stock2}", response_model=total_stock_correlation_model)
async def stock_correlation(stock1: str, stock2: str):
    totalCorr = TickerCorrelation.get_total_correlation(TickerCorrelation, stock1, stock2)
    # generate a new stock_correlation_model object
    return totalCorr

# # get the total correlation between two stocks for a month
# @app.get("/stock_correlation/{stock1}/{stock2}/{month}", response_model=monthly_stock_correlation_model)
# async def monthly_stock_correlation(stock1: str, stock2: str, month: str):
#     monthlyCorr = TickerCorrelation.get_monthly_correlation(TickerCorrelation, stock1, stock2, month)
#     # generate a new stock_correlation_model object
#     return monthly_stock_correlation_model(stock1=stock1, stock2=stock2, month=month, correlation=monthlyCorr)

# check if valid pairs
@app.get("/stock_correlation/{stock1}/{stock2}/valid_pairs", response_model=bool)
async def valid_pairs(stock1: str, stock2: str):
    validPairs = TickerCorrelation.get_valid_pairs(TickerCorrelation, stock1, stock2)
    # generate a new stock_correlation_model object
    return validPairs

# allow any request from any origin
origins = [
    "*"
]

# allow any request from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



