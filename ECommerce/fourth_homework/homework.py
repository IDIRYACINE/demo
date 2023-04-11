import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and read the data
df = pd.read_csv('e-commerce.csv')

# Check and display the information summary of the dataset
print(df.info())
print("#--------------------------")

# Print the number of missing data for each variable
print(df.isnull().sum())
print("#--------------------------")

# Print the number of duplicates for each variable
print(df.duplicated().sum())
print("#--------------------------")

# Handle duplicates by dropping them
df.drop_duplicates()
print("#--------------------------")


# Remove the missing data rows for <Product_Category_2>
df.dropna(subset=['Product_Category_2'], )
print("#--------------------------")

# Fill the missing data using the appropriate method for <Product_Category_3>
df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0], )
print("#--------------------------")

# Encode categorical variables using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Gender', 'City_Category', 'Age', 'Stay_In_Current_City_Years'])

# Show a random sample of 15 rows from the dataset
print(df_encoded.sample(n=15))
print("#--------------------------")

# Show the first 7 lines of the dataset
print(df_encoded.head(7))
print("#--------------------------")

# Show the last 3 lines of the dataset
print(df_encoded.tail(3))
print("#--------------------------")

# Create a 3D histogram plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

purchase = df['Purchase']
hist, xedges, yedges = np.histogram2d(purchase,np.ones(len(purchase)), bins=20)

# Construct arrays for the anchor positions of the bars
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 3

# Construct arrays with the dimensions for the bars
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

# Create the 3D bar plot
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

# Set the axis labels and title
ax.set_xlabel('Purchase')
ax.set_ylabel('Z')
ax.set_zlabel('Frequency')
ax.set_title('Distribution of Purchase')

# Show the plot
plt.show()

print("#--------------------------")

# Calculate summary statistics for each variable
summary_stats = df_encoded.describe()
print(summary_stats)

print("#--------------------------")

# Compare the distributions of the variables for different categories using groupby()
#'Age_0-17', 'Age_18-25','Age_26-35', 'Age_36-45', 'Age_46-50', 'Age_51-55', 'Age_55+'
grouped_data = df_encoded.groupby('Age_0-17')['Purchase'].describe()
print(grouped_data)

grouped_data = df_encoded.groupby('Age_18-25')['Purchase'].describe()
print(grouped_data)

grouped_data = df_encoded.groupby('Age_26-35')['Purchase'].describe()
print(grouped_data)

grouped_data = df_encoded.groupby('Age_46-50')['Purchase'].describe()
print(grouped_data)

grouped_data = df_encoded.groupby('Age_51-55')['Purchase'].describe()
print(grouped_data)

grouped_data = df_encoded.groupby('Age_55+')['Purchase'].describe()
print(grouped_data)
print("#--------------------------")
