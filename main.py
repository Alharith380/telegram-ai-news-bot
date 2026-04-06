#!/usr/bin/env python3
"""
Telegram AI News Bot - Main Entry Point
Fixed for Railway deployment
"""

import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

load_dotenv()
# Fix for Railway event loop issue
try:
    import nest_asyncio
    nest_asyncio.apply()
except ImportError:
    pass

from src.bot import run_bot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    print("=" * 50)
    print("🤖 بوت أخبار الذكاء الاصطناعي")
    print("=" * 50)
    print("جاري تشغيل البوت...")
    print("للإيقاف: Ctrl+C")
    print("=" * 50)
    sys.stdout.flush()

    try:
        asyncio.run(run_bot())
    except RuntimeError as e:
        if "event loop" in str(e).lower():
            # Fallback for environments with existing event loop
            loop = asyncio.get_event_loop()
            loop.run_until_complete(run_bot())
        else:
            raise
