import pandas as pd
import telethon
from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os
import re
import asyncio
import nest_asyncio
import csv

# Apply nest_asyncio to avoid issues with event loops in interactive environments
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title
    print(f"Scraping data from channel: {channel_title}")

    count = 0  # To count the number of messages scraped
    async for message in client.iter_messages(entity, limit=10000):
        media_path = None

        if message.media and hasattr(message.media, 'photo'):
            # Create a unique filename for the photo
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            # Download the media to the specified directory if it's a photo
            await client.download_media(message.media, media_path)

        # Extract text from the message
        text = message.text if message.text else ""

        # Write message data to CSV (using writer for lists)
        writer.writerow([channel_title, message.id, message.date, text, media_path])

        count += 1

    print(f"Finished scraping {count} messages from {channel_username}.\n")

# Function to preprocess text data
def preprocess_text(text):
    # Remove special characters and punctuation
    text = re.sub(r"[^\w\s]", "", text)

    print(f"Preprocessing text: {text[:50]}...")  # Show first 50 characters for preview
    return text  # Returning the text itself for simplicity

# Function to label a subset of the dataset in CoNLL format
def label_dataset(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for index, row in data.iterrows():
            text = row['preprocessed_text']
            # Tokenize the text and label entities manually or using a pre-trained NER model
            # Here we simply label them as O (outside any entity) for demonstration purposes
            for token in text.split():
                f.write(f"{token}\tO\n")
            f.write("\n")
        print(f"Saved labeled data in CoNLL format to {output_file}.")

# Function to ensure the client is connected and authenticated
async def ensure_connection(client):
    try:
        await client.start()  # Automatically connect and authorize
        print("Client successfully connected and authorized.")
    except Exception as e:
        print(f"Failed to connect: {e}")
        raise

# Main function
async def main():
    # Load channels from CSV and assign header manually
    channels_data = pd.read_csv('channels_to_crawl.csv', header=None, names=['channel_username'])
    print(f"Loaded {len(channels_data)} channels from channels_to_crawl.csv")

    # Create a Telegram client
    client = TelegramClient(phone, api_id, api_hash)

    try:
        # Ensure the client is connected and authorized
        await ensure_connection(client)

        # Create a directory to store media files
        media_dir = 'media'
        os.makedirs(media_dir, exist_ok=True)
        print(f"Created directory for media files: {media_dir}")

        # Iterate over channels and scrape data
        for index, row in channels_data.iterrows():
            channel_username = row['channel_username']
            print(f"Scraping {channel_username}...")

            # Use csv.writer instead of DictWriter
            with open(f"{channel_username}.csv", 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['channel_title', 'message_id', 'date', 'text', 'media_path'])  # Header row

                await scrape_channel(client, channel_username, writer, media_dir)

            print(f"Data scraped for {channel_username}. Saved to {channel_username}.csv.\n")

        # Load the scraped data into a DataFrame
        data = pd.read_csv('telegram_data.csv')  # Adjust the file path if necessary
        print(f"Loaded {len(data)} rows of data from telegram_data.csv")

        # Preprocess the text data
        data['preprocessed_text'] = data['text'].apply(preprocess_text)
        print("Text data preprocessing completed.\n")

        # Label a subset of the data
        label_dataset(data.head(50), 'labeled_telegram_data_conll.txt')  # Adjust the number of samples
        print("Labeling of data completed.\n")

    except ConnectionError as e:
        print(f"ConnectionError: {e}")
    finally:
        # Always disconnect the client when done
        await client.disconnect()

# Helper function to run the asynchronous main in an environment with a running event loop
def run_main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Run the main function in environments with an already running event loop
run_main()
