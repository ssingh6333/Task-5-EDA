import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("All libraries are installed successsfully")
df=pd.read_csv('Sales data.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())
#Duplicate data
df=df.drop(columns=['CusName', 'Total Amount'])
#total sales per product nd also showing highest selling product..
sns.barplot(x='ProductList', y='Quant', data=df)
plt.show()
#average order value
avg_order_value = df['TotalAmount'].mean()
print("Average Order Value (AOV):", avg_order_value)
#customer purchasing some ,multiple products
customer_orders = df['CustomerName'].value_counts()
sns.barplot(x=customer_orders.index, y=customer_orders.values)
plt.title('Customer Order Frequency')
plt.show()
#price vs quantity sold
sns.scatterplot(x='PriceItem', y='Quant', data=df)
plt.title('Price vs Quantity Sold')
plt.show()
#outlier detection
sns.boxplot(x=df['TotalAmount'])
plt.title('Outliers in Total Sales Amount')
plt.show()
#correlation
sns.regplot(x='PriceItem', y='TotalAmount', data=df)
plt.title('Price vs Total Sales Value')
plt.show()




