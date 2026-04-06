#!/usr/bin/env python3
"""
Daily AI News Sender - Arabic with Images
Handles multiple users including blocked ones gracefully
"""

import asyncio
import json
import os
from telegram import Bot
from telegram.error import Forbidden, RetryAfter, TimedOut

# Bot token
BOT_TOKEN = ""
SUBSCRIBERS_FILE = 'data/subscribers.json'

# Arabic AI News with images
NEWS_ITEMS = [
    {
        "title": "🇨🇳 الصين تطلب إيقاف طلبات رقائق Nvidia H200",
        "desc": "طلبت الصين من شركات التكنولوجيا إيقاف طلبات رقائق Nvidia H200 للذكاء الاصطناعي.\n\n• القرار يشمل شركات صينية كبرى\n• يأتي في ظل التوترات التجارية",
        "img": "https://www.chosun.com/resizer/v2/XBQU65AA7FEMVH62PPKKVM6TV4.jpg?auth=037a4bfad4b80e51667793a47b55a8304c541befbed5dc8857566cf6341d7a5b&width=616",
        "source": "Reuters"
    },
    {
        "title": "🔵 ميتا تستحوذ على Manus للذكاء الاصطناعي",
        "desc": "استحوذت Meta على شركة Manus الناشئة للذكاء الاصطناعي.\n\n• الصفقة تبلغ حوالي 2-3 مليار دولار\n• Manus متخصصة في وكلاء AI",
        "img": "https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/1272/cached.offlinehbpl.hbpl.co.uk/news/KMP/Untitleddesign-2026-01-02T092013.479.png",
        "source": "BBC Tech"
    },
    {
        "title": "👓 جوجل تستعد لإطلاق نظارات AI في 2026",
        "desc": "تستعد جوجل لإطلاق نظارات ذكاء اصطناعي جديدة.\n\n• النظارات مزودة بتقنية Gemini AI\n• تعاون مع Warby Parker",
        "img": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ivNytzZUiU00/v1/-1x-1.webp",
        "source": "TechCrunch"
    },
    {
        "title": "🎵 سبوتيفاي تختبر قوائم تشغيل AI مخصصة",
        "desc": "تختبر سبوتيفاي ميزات جديدة للذكاء الاصطناعي في قوائم التشغيل.\n\n• قوائم تشغيل AI أكثر تخصيصاً\n• ميزة Prompted Playlists",
        "img": "https://storage.googleapis.com/pr-newsroom-wp/1/2023/02/FTR-Header-DJ-1-1.png",
        "source": "TechCrunch"
    },
    {
        "title": "🤖 ElevenLabs تصل قيمة 6.6 مليار دولار",
        "desc": "حققت شركة ElevenLabs للذكاء الاصطناعي الصوتي قفزة كبيرة في قيمتها.\n\n• القيمة وصلت إلى 6.6 مليار دولار\n• توسع في نطاق الخدمات",
        "img": "https://images.squarespace-cdn.com/content/v1/5fac380b9cda2c532cffb9e8/e5a5d6fe-85c8-49f3-96dd-85836de8e981/chatgpt.jpg",
        "source": "TechCrunch"
    }
]


def load_subscribers():
    """Load subscriber chat IDs"""
    try:
        if os.path.exists(SUBSCRIBERS_FILE):
            with open(SUBSCRIBERS_FILE, 'r') as f:
                data = json.load(f)
                return data.get('chat_ids', [])
    except:
        pass
    return []


def remove_blocked_user(chat_id: int):
    """Remove a blocked user from subscribers"""
    subscribers = load_subscribers()
    if chat_id in subscribers:
        subscribers.remove(chat_id)
        with open(SUBSCRIBERS_FILE, 'w') as f:
            json.dump({'chat_ids': subscribers}, f)
        print(f"  🗑️ تم إزالة المستخدم المحظور: {chat_id}")


async def send_news_to_user(bot: Bot, chat_id: int):
    """Send Arabic news with images to a specific user"""

    # Welcome message
    welcome = """🎉 *مرحباً بك في أخبار الذكاء الاصطناعي!*

📰 *آخر أخبار الذكاء الاصطناعي اليومية:*
━━━━━━━━━━━━━━━"""

    await bot.send_message(chat_id=chat_id, text=welcome, parse_mode='Markdown')
    await asyncio.sleep(1)

    # Send news with images
    for news in NEWS_ITEMS:
        caption = f"*{news['title']}*\n\n{news['desc']}\n🔗 {news['source']}"

        try:
            await bot.send_photo(
                chat_id=chat_id,
                photo=news['img'],
                caption=caption,
                parse_mode='Markdown'
            )
        except Forbidden:
            # User blocked the bot
            raise
        except Exception as e:
            # Send without image if other error
            try:
                await bot.send_message(
                    chat_id=chat_id,
                    text=caption,
                    parse_mode='Markdown'
                )
            except Forbidden:
                raise
            except:
                pass

        await asyncio.sleep(0.5)

    # Footer
    footer = """
━━━━━━━━━━━━━━━
📌 *أوامر البوت:*

/start - عرض الأخبار من جديد
/news - جلب آخر الأخبار

📅 *النشرة اليومية:*
يومياً الساعة 8 صباحاً

⚡ *بوت أخبار الذكاء الاصطناعي*"""

    await bot.send_message(chat_id=chat_id, text=footer, parse_mode='Markdown')


async def send_daily_news():
    """Send daily news to all subscribers"""
    print("=" * 50)
    print("🤖 بدء إرسال النشرة اليومية...")
    print("=" * 50)

    bot = Bot(token=BOT_TOKEN)
    subscribers = load_subscribers()

    if not subscribers:
        print("⚠️ لا يوجد مشتركين. شارك رابط البوت مع الآخرين!")
        return

    print(f"📋 عدد المشتركين: {len(subscribers)}")

    success_count = 0
    blocked_count = 0

    for chat_id in subscribers:
        try:
            print(f"📤 إرسال الأخبار للمستخدم {chat_id}...")
            await send_news_to_user(bot, chat_id)
            print(f"  ✅ تم الإرسال بنجاح!")
            success_count += 1
        except Forbidden:
            print(f"  ⚠️ المستخدم {chat_id} حظر البوت - سيتم إزالته")
            remove_blocked_user(chat_id)
            blocked_count += 1
        except RetryAfter as e:
            print(f"  ⏳ انتظار {e.retry_after} ثانية...")
            await asyncio.sleep(e.retry_after)
        except TimedOut:
            print(f"  ⏰ انتهاء المهلة - سيتم إعادة المحاولة لاحقاً")
        except Exception as e:
            print(f"  ❌ خطأ: {str(e)[:50]}")

    print("=" * 50)
    print(f"✅ تم الإرسال لـ {success_count}/{len(subscribers)} مشترك")
    if blocked_count > 0:
        print(f"🗑️ تم إزالة {blocked_count} مستخدم محظور")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(send_daily_news())
