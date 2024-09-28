from telethon import TelegramClient

def fetch_messages(api_id, api_hash, channel_list):
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    messages = []
    for channel in channel_list:
        for message in client.iter_messages(channel):
            if message.text:
                messages.append({
                    'channel': channel,
                    'message': message.text,
                    'timestamp': message.date
                })
    return messages

if __name__ == "__main__":
    api_id = 'your_api_id'
    api_hash = 'your_api_hash'
    channel_list = ['@Channel1', '@Channel2']
    messages = fetch_messages(api_id, api_hash, channel_list)
    # Save raw data
    with open('data/raw/telegram_messages.json', 'w') as f:
        json.dump(messages, f)
