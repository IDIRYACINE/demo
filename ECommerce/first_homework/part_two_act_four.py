import pandas as pd
import csv

def compute_average_age_and_grade():
    df = pd.read_csv('./data/students.csv')

    avg_age = df['age'].mean()
    avg_grade = df['grade'].mean()

    print("Average Age: ", avg_age)
    print("Average Grade: ", avg_grade)

def load_books_and_do_various_computations():
    books_dict = {}
    with open('./data/books.csv') as csvfile:
        reader = csv.reader(csvfile)

        next(reader) # skip header

        for row in reader:
            books_dict[row[0]] = {'author': row[1], 'year_published': int(row[2]), 'rating': float(row[3])}

    books_df = pd.DataFrame.from_dict(books_dict, orient='index')

    avg_ratings = books_df.groupby('author')['rating'].mean()
    print("Average rating for each author:\n", avg_ratings)

    print('#----------------------------------------#')

    highest_avg_rating_author = avg_ratings.idxmax()
    print("Author with the highest average rating:", highest_avg_rating_author)

    print('#----------------------------------------#')
    overall_avg_rating = books_df['rating'].mean()
    print("Overall average rating:", overall_avg_rating)
    print('#----------------------------------------#')

    high_rated_books_df = books_df[books_df['rating'] >= overall_avg_rating]
    print("Books with rating greater than or equal to overall average rating:\n", high_rated_books_df)

compute_average_age_and_grade()
print('#----------------------------------------#')
load_books_and_do_various_computations()