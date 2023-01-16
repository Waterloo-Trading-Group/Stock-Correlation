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



