import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('EcommerceDataset.csv')

# Check the dataset for missing values and handle them appropriately
print(df.isnull().sum())  # Check for missing values in each column
df.dropna()   # Drop rows with missing values

# Check the dataset for duplicates and handle them appropriately
print(df.duplicated().sum())  # Check for duplicates
df.drop_duplicates()  # Drop duplicates

# Convert the Order_Date column to a datetime data type
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Explore the data to identify the different product categories and products in the dataset
unique_categories = df['Product_Category'].unique()
print(unique_categories)

unique_products = df['Product'].unique()
print(unique_products)

# Calculate the total sales and profit for each product category and product
sales_profit = df.groupby(['Product_Category', 'Product'])['Sales', 'Profit'].sum()
print(sales_profit)

# Visualize the total sales and profit for each product category and product using bar charts
sales_profit.plot(kind='bar', edgecolor="black",figsize=(12, 6))
plt.title('Total Sales and Profit by Product Category and Product')
plt.xlabel('Product Category, Product')
plt.ylabel('Total Sales and Profit')
plt.show()

# Analyze and visualize the distribution of the shipping cost and profit
df[['Shipping_Cost', 'Profit']].hist(edgecolor="black",figsize=(10, 5))
plt.suptitle('Distribution of Shipping Cost and Profit')
plt.show()


# Identify the most popular payment methods used by customers
payment_methods = df['Payment_method'].value_counts()
print(payment_methods)

# Analyze and visualize the distribution of the aging of the orders
df['Order_Date'] = pd.to_datetime(df['Order_Date'])  # convert to Timestamp object
df['Order_Age'] = (pd.to_datetime('today') - df['Order_Date']).dt.days
df['Order_Age'].hist(edgecolor="black")
plt.title('Distribution of Order Age')
plt.xlabel('Order Age (days)')
plt.ylabel('Count')
plt.show()

# Explore the relationship between the device type and the order priority
device_order_priority = df.groupby(['Device_Type', 'Order_Priority'])["Time"].count()
device_order_priority.plot(kind='bar', edgecolor="black",figsize=(10, 5))
plt.title('Device Type vs. Order Priority')
plt.xlabel('Device Type, Order Priority')
plt.ylabel('Count')
plt.show()

# Explore the relationship between the product category, product, and sales
category_product_sales = df.groupby(['Product_Category', 'Product'])['Sales'].sum()
category_product_sales.plot(kind='bar', edgecolor="black",figsize=(10, 5))
plt.title('Product Category, Product vs. Sales')
plt.xlabel('Product Category, Product')
plt.ylabel('Sales')
plt.show()
