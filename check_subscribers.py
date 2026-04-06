#!/usr/bin/env python3
"""Check and update subscribers from bot updates"""
import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Bot
import json
import asyncio

async def check_subscribers():
    bot = Bot(token='')

    # Get all updates to find subscribers
    updates = await bot.get_updates()

    subscribers = set()
    for update in updates:
        if update.message:
            subscribers.add(update.message.chat.id)
            print(f"Found message from: {update.message.chat.id} ({update.message.chat.username or 'no username'})")
        if update.callback_query:
            subscribers.add(update.callback_query.chat.id)
            print(f"Found callback from: {update.callback_query.chat.id}")

    # Also add known subscriber
    subscribers.add()

    print(f"\n📋 Total subscribers: {len(subscribers)}")
    print(f"IDs: {subscribers}")

    # Save to file
    with open('/workspace/telegram-ai-news-bot/data/subscribers.json', 'w') as f:
        json.dump({'chat_ids': list(subscribers)}, f)

    print("✓ Updated subscribers file")
    return subscribers

if __name__ == "__main__":
    asyncio.run(check_subscribers())
