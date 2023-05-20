from os import path
from pyrogram import Client, filters
import csv

# в файл config.ini потрібно вписати api_id, api_hash, та дані для проксі.
app = Client("account")

key_words = {"test", "test2", "test3"}


def save_message(message):
    headers = ["Chat name", "Time", "Message"]
    file_exists = path.exists("intercept_message.csv")
    with open("intercept_message.csv", 'a',  encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists or f.tell() == 0:
            writer.writerow(headers)
        writer.writerow([message.chat.title, message.date, message.caption if message.text is None else message.text])


@app.on_message(filters.text | filters.photo)
def parse(client, message):
    if any(word in (message.text or '') or word in (message.caption or '') for word in key_words):
        save_message(message)


app.run()
