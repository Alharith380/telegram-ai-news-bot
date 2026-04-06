#!/usr/bin/env python3
"""Send Arabic AI News Report with Images to Telegram"""

from telegram import Bot
import asyncio

async def send_arabic_report():
    bot = Bot(token='')
    chat_id = 5839261109

    # Arabic header
    header = """🤖 *تقرير أخبار الذكاء الاصطناعي*
📅 26 مارس 2026
━━━━━━━━━━━━━━━"""

    await bot.send_message(chat_id=chat_id, text=header)
    print("✓ تم إرسال العنوان")

    # News 1 - China Nvidia
    msg1 = """🇨🇳 *الصين تطلب إيقاف طلبات رقائق Nvidia H200*

طلبت الصين من شركات التكنولوجيا إيقاف طلبات رقائق Nvidia H200 للذكاء الاصطناعي.

📌 التفاصيل:
• القرار يشمل شركات صينية كبرى
• قد تفرض الصين قواعد جديدة للاستخدام المحلي
• يأتي في ظل التوترات التجارية الأمريكية الصينية

🔗 Reuters"""
    try:
        await bot.send_photo(
            chat_id=chat_id,
            photo='https://www.chosun.com/resizer/v2/XBQU65AA7FEMVH62PPKKVM6TV4.jpg?auth=037a4bfad4b80e51667793a47b55a8304c541befbed5dc8857566cf6341d7a5b&width=616',
            caption=msg1,
            parse_mode='Markdown'
        )
        print("✓ تم إرسال خبر 1")
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=msg1)
        print(f"خبر 1 (بدون صورة): {e}")

    # News 2 - Meta Manus
    msg2 = """🔵 *ميتا تستحوذ على Manus للذكاء الاصطناعي*

استحوذت Meta على شركة Manus الناشئة للذكاء الاصطناعي.

📌 التفاصيل:
• الصفقة تبلغ حوالي 2-3 مليار دولار
• Manus متخصصة في وكلاء الذكاء الاصطناعي
• تعكس اهتمام ميتا بتطوير تقنيات AI

🔗 BBC Tech"""
    try:
        await bot.send_photo(
            chat_id=chat_id,
            photo='https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/1272/cached.offlinehbpl.hbpl.co.uk/news/KMP/Untitleddesign-2026-01-02T092013.479.png',
            caption=msg2,
            parse_mode='Markdown'
        )
        print("✓ تم إرسال خبر 2")
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=msg2)
        print(f"خبر 2 (بدون صورة): {e}")

    # News 3 - Google Glasses
    msg3 = """👓 *جوجل تستعد لإطلاق نظارات AI في 2026*

تستعد جوجل لإطلاق نظارات ذكاء اصطناعي جديدة.

📌 التفاصيل:
• النظارات مزودة بتقنية Gemini AI
• تعاون مع Warby Parker للتصميم
• عودة لنظارات جوجل بتقنيات محسنة

🔗 TechCrunch"""
    try:
        await bot.send_photo(
            chat_id=chat_id,
            photo='https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ivNytzZUiU00/v1/-1x-1.webp',
            caption=msg3,
            parse_mode='Markdown'
        )
        print("✓ تم إرسال خبر 3")
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=msg3)
        print(f"خبر 3 (بدون صورة): {e}")

    # News 4 - ElevenLabs
    msg4 = """🎙️ *ElevenLabs تصل قيمة إلى 6.6 مليار دولار*

حققت شركة ElevenLabs للذكاء الاصطناعي الصوتي قفزة كبيرة في قيمتها.

📌 التفاصيل:
• القيمة وصلت إلى 6.6 مليار دولار
• CEO: الأرباح الحقيقية ليست في الصوت فقط
• الشركة توسع نطاق خدماتها

🔗 TechCrunch"""
    try:
        await bot.send_photo(
            chat_id=chat_id,
            photo='https://eleven-public-cdn.elevenlabs.io/_next/image?url=https%3A%2F%2Feleven-public-cdn.elevenlabs.io%2Fpayloadcms%2Fvoice-design-cover-1.webp&w=3840&q=95',
            caption=msg4,
            parse_mode='Markdown'
        )
        print("✓ تم إرسال خبر 4")
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=msg4)
        print(f"خبر 4 (بدون صورة): {e}")

    # News 5 - Spotify AI
    msg5 = """🎵 *سبوتيفاي تختبر قوائم تشغيل AI مخصصة*

تختبر سبوتيفاي ميزات جديدة للذكاء الاصطناعي في قوائم التشغيل.

📌 التفاصيل:
• قوائم تشغيل AI أكثر تخصيصاً
• ميزة "Prompted Playlists"
• تكنولوجيا متقدمة للتوصيات

🔗 TechCrunch"""
    try:
        await bot.send_photo(
            chat_id=chat_id,
            photo='https://storage.googleapis.com/pr-newsroom-wp/1/2023/02/FTR-Header-DJ-1-1.png',
            caption=msg5,
            parse_mode='Markdown'
        )
        print("✓ تم إرسال خبر 5")
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=msg5)
        print(f"خبر 5 (بدون صورة): {e}")

    # Footer
    footer = """━━━━━━━━━━━━━━━
⚡ *نُشر بواسطة بوت أخبار الذكاء الاصطناعي*
🔄 التحديث التالي: غداً الساعة 8 صباحاً"""
    await bot.send_message(chat_id=chat_id, text=footer)
    print("✓ تم إرسال الفوتر")

    print("\n✅ تم إرسال التقرير كاملاً!")

if __name__ == "__main__":
    asyncio.run(send_arabic_report())
