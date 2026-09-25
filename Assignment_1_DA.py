# 1.Create a 1D Numpy array
import numpy as np
temperatures_w1 = np.array([22.5,25.3,20.8,23.4,26.1,24.8,21.9])

# Inspection and Properties
print("Shape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)

# 3.Array Operations
farenheit_w1 = (temperatures_w1 * 9/5) + 32
print("Fahrenheit values:", farenheit_w1)

print("Max:", temperatures_w1.max())
print("Min:", temperatures_w1.min())
print("Mean:", temperatures_w1.mean())

# 4.Array Slicing and Indexing
first_three = temperatures_w1[:3]
weekend = temperatures_w1[-2:]
middle_three = temperatures_w1[2:5]

# 5.Create a 2D Array
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9], 
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]   
])

# 6.Inspect and Slice the 2D Array
print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Number of elements:", temperatures.size)

week1 = temperatures[0]
week2 = temperatures[1]
weekend_week1 = temperatures[0, -2:]
weekend_week2 = temperatures[1, -2:]

# 1.Creating Panda Series
import pandas as pd

marks = pd.Series(
    [95,92,89,85,80],
    index=['Rank1','Rank2','Rank3','Rank4','Rank5']
)

# 2. Indexing and Slicing
first_rank_mark = marks.iloc[0]
top_3 = marks.loc[['Rank1','Rank2','Rank3']]
third_rank_mark = marks.iloc[2]
above_90 = marks[marks > 90]

# 3. Manipulating Series
marks['Rank1'] = 100
marks = marks.drop('Rank5')
cgpa = marks / 10

# 1.Creating Pandas DataFrame
transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing',
                         'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

# 2.Data_Exploration
print(transactions.head())
print(transactions.tail())
print(transactions.shape)
print(transactions.columns)
print(transactions.dtypes)

transactions[['ProductCategory', 'Amount']]

transactions.iloc[:, -3:]
filtered = transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)]

transactions['ProductCategory'].value_counts()

transactions['Region'].unique()

transactions.groupby('Region')['Amount'].mean()

# 3. Manipulating and DataFrame
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
transactions['Discount'] = transactions['Amount'] * 0.10
transactions = transactions[transactions['TransactionID'] != 109]
transactions = transactions.drop(columns=['Discount'])