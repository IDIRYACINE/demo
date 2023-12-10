# Mount Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

# Import libraries
import pandas as pd
from spellchecker import SpellChecker

# Define the spell checker function
def spell_correction(tokens):
    spell = SpellChecker()
    corrected_tokens = [spell.correction(token) for token in tokens]
    return ' '.join(corrected_tokens)

# Update file paths
file_path = '/content/gdrive/My Drive/Path/To/Your/File/preprocessed.csv'
output_file_path = '/content/gdrive/My Drive/Path/To/Your/File/preprocessed_corrected.csv'

# Read the CSV file
df = pd.read_csv(file_path, encoding='utf-8')

# Apply spell correction to the tokens column
tokens = df['tokens']
tokens = tokens.apply(spell_correction)
df['tokens'] = tokens

# Save the corrected data
df.to_csv(output_file_path, index=False, encoding='utf-8')

print("Spell correction complete! Corrected data saved to", output_file_path)
