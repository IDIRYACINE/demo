# import pandas library
import pandas as pd
import matplotlib.pyplot as plt

# load and read the data
df = pd.read_csv('./data/Thestudents.csv')

# check the dimensions of the dataset
print('Dimensions of the dataset:', df.shape)

# print the number of missing data for each variable
print('Number of missing data for each variable:')
print(df.isnull().sum())

# print the number of duplicates for each variable
print('Number of duplicates for each variable:')
print(df.duplicated().sum())

# handle missing data by removing rows
df_removed = df.dropna()
print('\nAfter removing missing data:')
print('Dimensions of the dataset:', df_removed.shape)
print('#----------------------------------------#')

# handle missing data by filling with appropriate method for each variable
df_filled = df.fillna({'Gender': df['Gender'].mode()[0], 'Age': df['Age'].mean(),
                       'Height': df['Height'].median(), 'Weight': df['Weight'].median()})
print('\nAfter filling missing data:')
print('Dimensions of the dataset:', df_filled.shape)
print('#----------------------------------------#')


# handle duplicates
df_unique = df_filled.drop_duplicates()
print('\nAfter handling duplicates:')
print('Dimensions of the dataset:', df_unique.shape)
print('#----------------------------------------#')

# show a random sample of 23 rows from the dataset
print('\nRandom sample of 23 rows from the dataset:')
print(df_unique.sample(23))
print('#----------------------------------------#')

# show the first 3 lines of the dataset
print('\nThe first 3 lines of the dataset:')
print(df_unique.head(3))
print('#----------------------------------------#')

# show the last 5 lines of the dataset
print('\nThe last 5 lines of the dataset:')
print(df_unique.tail(5))
print('#----------------------------------------#')


# 10. Who are the 3 oldest students? (list their names)
oldest_students = df_unique.nlargest(3, 'Age')['Name'].tolist()
print('\nThe 3 oldest students are:', oldest_students)
print('#----------------------------------------#')

# 11. Who are the students with the highest grades? (list their names)
highest_grades = df_unique.nlargest(3, 'Grade')['Name'].tolist()
print('\nThe students with the highest grades are:', highest_grades)
print('#----------------------------------------#')

# 12. What are the grades of the 10 youngest students?
youngest_grades = df_unique.nsmallest(10, 'Age')[['Name', 'Grade']]
print('\nThe grades of the 10 youngest students:')
print(youngest_grades)
print('#----------------------------------------#')

# 13. Show in a pie chart the percentage of each gender in the dataset
gender_counts = df_unique['Gender'].value_counts()
labels = ['Male', 'Female']
plt.pie(gender_counts, labels=labels, autopct='%1.1f%%')
plt.title('Gender Percentage')
plt.show()
print('#----------------------------------------#')

# 14. Show in a bar chart the distribution of the students' grades
grades_counts = df_unique['Grade'].value_counts()
plt.bar(grades_counts.index, grades_counts.values)
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.title('Grades Distribution')
plt.show()
print('#----------------------------------------#')

# 15. Show in a histogram the distribution of the students’ age
plt.hist(df_unique['Age'], bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
print('#----------------------------------------#')
