import contractions
import re

def expand_contractions(text):
    expanded_text = contractions.fix(text)

    return expanded_text

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_text_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Expanded text has been written to '{file_path}'.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    input_file_path = 'input.txt'
    output_file_path = 'expanded_text.txt'

    original_text = read_text_file(input_file_path)

    if original_text:
        expanded_text = expand_contractions(original_text)

        write_text_file(output_file_path, expanded_text)


def expand_contractions_custom(text):
    # Define a dictionary of contraction expansions
    contraction_rules = {
        "I'm": 'I am',
        "you're": 'you are',
        "he's": 'he is',
        "she's": 'she is',
        "it's": 'it is',
        "we're": 'we are',
        "they're": 'they are',
        "I've": 'I have',
        "you've": 'you have',
        "we've": 'we have',
        "they've": 'they have',
        "I'll": 'I will',
        "you'll": 'you will',
        "he'll": 'he will',
        "she'll": 'she will',
        "it'll": 'it will',
        "we'll": 'we will',
        "they'll": 'they will',
        "I'd": 'I would',
        "you'd": 'you would',
        "he'd": 'he would',
        "she'd": 'she would',
        "it'd": 'it would',
        "we'd": 'we would',
        "they'd": 'they would',
        "isn't": 'is not',
        "aren't": 'are not',
        "wasn't": 'was not',
        "weren't": 'were not',
        "hasn't": 'has not',
        "haven't": 'have not',
        "hadn't": 'had not',
        "won't": 'will not',
        "wouldn't": 'would not',
        "don't": 'do not',
        "doesn't": 'does not',
        "didn't": 'did not',
        "can't": 'cannot',
        "couldn't": 'could not',
        "shouldn't": 'should not',
        "mightn't": 'might not',
        "mustn't": 'must not'
        # Add more rules as needed
    }

    # Use regex to find and replace contractions in the text
    for contraction, expansion in contraction_rules.items():
        text = re.sub(r'\b' + re.escape(contraction) + r'\b', expansion, text)

    return text

def main2() : 
    text_with_contractions = "I can't believe you're here. It's a beautiful day, isn't it?"
    expanded_text = expand_contractions_custom(text_with_contractions)

    print("Original text:")
    print(text_with_contractions)
    print("\nText after expanding contractions:")
    print(expanded_text)

main2()