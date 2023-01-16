#!/usr/bin/env python3
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf


class TickerCorrelation:
	"""Manages program"""

	def __init__(self):
		"""Initializes program and creates resources"""
		df = pd.DataFrame()
		corr_df = pd.DataFrame()
		corr_df2 = pd.DataFrame() 
		corr_df3 = pd.DataFrame()
		corr_df4 = pd.DataFrame()
		corr_df5 = pd.DataFrame()
		df_master = pd.DataFrame()
		stock1 = ''
		stock2 = ''
	
	# get kendall correlation between historic stock prices
	def get_total_correlation(self, stock1, stock2):
		"""Prompts user to input stocks"""
		#API to get data from Yahoo
		# stock_data = {ticker: web.get_data_yahoo(ticker) for ticker in [self.stock1, self.stock2]}
		# self.df = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in stock_data.items()})
		stock_data = {ticker: yf.download(ticker) for ticker in [stock1, stock2]}
		self.df = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in stock_data.items()})
		#Convert the index to date
		self.df.index = pd.to_datetime(self.df.index)

		#Create month and year columns
		self.df['month'] = self.df.index.month
		self.df['year'] = self.df.index.year

		#Create a new dataframe with the monthly average
		self.corr_df = self.df.groupby(['month', 'year']).mean()
		
		# Kendal Correlation
		self.corr_df2 = self.corr_df.pct_change().corr(method='kendall')
		# Pearsons Correlation
		self.corr_df3 = self.corr_df.pct_change().corr(method='pearson')
		# Spearman Correlation
		self.corr_df4 = self.corr_df.pct_change().corr(method='spearman')

		jsonObj = { 
			"Kendall": self.corr_df2[stock1][stock2],
			"Pearson": self.corr_df3[stock1][stock2],
			"Spearman": self.corr_df4[stock1][stock2],
		}

		return jsonObj



