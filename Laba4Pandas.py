import pandas as pd
import numpy as np

Data_Listings = pd.read_csv('listings.csv')
# print(Data_Listings)
# print(Data_Listings.head())
# print(Data_Listings.tail())
print(Data_Listings.describe())
Data_Listings = Data_Listings.iat[1, 1]
print(Data_Listings.describe())
Data_Listings_Dropna = Data_Listings.dropna()
Data_Listings_Fill = Data_Listings.fillna(0)
# print(Data_Listings_Dropna.describe())
# print(Data_Listings_Fill.describe())
