import pandas as pd
import langid
import json



def preprocess_csv_dataset(file_path):
    df = pd.read_csv(file_path, encoding='utf-8')
    

def describe_csv_dataset(file_path):
    df = pd.read_csv(file_path, encoding='utf-8')

    num_reviews = len(df)
    num_labels = df['sentiment'].nunique()
    max_review_length = df['review'].apply(len).max()
    min_review_length = df['review'].apply(len).min()
    average_review_length = df['review'].apply(len).mean()
    languages = set()

    for review in df['review']:
        lang, confidence = langid.classify(review)
        languages.add(lang)

    print(f"Number of reviews: {num_reviews}")
    print(f"Number of labels: {num_labels}")
    # print(f"Languages: {', '.join(languages)}")
    print(f"Maximum review length: {max_review_length} characters")
    print(f"Minimum review length: {min_review_length} characters")
    print(f"Average review length: {average_review_length} characters")

    results = {
        'num_reviews': num_reviews,
        'num_labels': num_labels,
        'languages': list(languages),
        'max_review_length': max_review_length,
        'min_review_length': min_review_length,
        'average_review_length': average_review_length
    }

    with open('output/step1.json', 'w') as f:
        json.dump(results, f)


    

# Example usage:
file_path = 'source.csv'  # Replace with the actual path to your CSV file
describe_csv_dataset(file_path)
