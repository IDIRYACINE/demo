import pandas as pd
import matplotlib.pyplot as plt

# Load and read the data
df = pd.read_csv('e-commerce.csv')

# Check and display the information summary of the dataset
print(df.info())

# Print the number of missing data for each variable
print(df.isnull().sum())

# Print the number of duplicates for each variable
print(df.duplicated().sum())

# Handle duplicates by dropping them
df.drop_duplicates(inplace=True)


# Remove the missing data rows for <Product_Category_2>
df.dropna(subset=['Product_Category_2'], inplace=True)

# Fill the missing data using the appropriate method for <Product_Category_3>
df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0], inplace=True)

# Encode categorical variables using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Gender', 'City_Category', 'Age', 'Stay_In_Current_City_Years'])

# Show a random sample of 15 rows from the dataset
print(df_encoded.sample(n=15))

# Show the first 7 lines of the dataset
print(df_encoded.head(7))

# Show the last 3 lines of the dataset
print(df_encoded.tail(3))

plt.hist(df_encoded['Purchase'], bins=20)
plt.xlabel('Purchase')
plt.ylabel('Frequency')
plt.title('Distribution of Purchase')
plt.show()

# Calculate summary statistics for each variable
summary_stats = df_encoded.describe()
print(summary_stats)

# Compare the distributions of the variables for different categories using groupby()
grouped_data = df_encoded.groupby(['Age', 'Gender'])['Purchase'].mean().reset_index()
print(grouped_data)
