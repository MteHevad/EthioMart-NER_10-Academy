import pandas as pd
import re

def clean_message(message):
    # Amharic-specific text cleaning
    message = re.sub(r'\d+', '', message)  # Remove numbers
    message = re.sub(r'[^\w\s]', '', message)  # Remove punctuation
    return message.strip()

def preprocess_data(input_file, output_file):
    df = pd.read_json(input_file)
    df['clean_message'] = df['message'].apply(clean_message)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    preprocess_data('data/raw/telegram_messages.json', 'data/processed/telegram_preprocessed.csv')
