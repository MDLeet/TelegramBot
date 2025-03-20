import re
from telethon.sync import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument, MessageMediaWebPage
from deep_translator import GoogleTranslator

# بيانات API الخاصة بتليجرام
api_id = 12345678  # استبدل بـ API ID الخاص بك
api_hash = '1232123123123212321231232123212321'  # استبدل بـ API Hash الخاص بك

# معرفات القنوات المصدر
source_channels = [-123321231321, -123321231321, -123321231321]  # استبدل بالقنوات التي تريد مراقبتها
# معرف القناة المستهدفة في تيليجرام
destination_channel = -123321231321  # استبدل بالقناة التي سيتم نشر الأخبار فيها

# هاشتاجات مخصصة
hashtags = "#telegram #bot #coded #by #MDLeet"

# إنشاء جلسة تيليجرام
client = TelegramClient('New_session', api_id, api_hash)

def clean_text(text):
    """ تنظيف النص من Markdown غير الصحيح وإصلاح التنسيق """
    if not text:
        return ""  # تجنب الأخطاء إذا كان النص فارغًا

    text = text.strip()  # إزالة أي فراغات زائدة
    
    # حذف أي روابط في بداية النص بصيغة [] (الرابط)
    text = re.sub(r"^\[\]\s*\(https?://[^\)]+\)\s*", "", text)

    return text

def translate_text(text):
    """ ترجمة النص مع الحفاظ على الكلمات الإنجليزية """
    try:
        if not text:
            return ""  # تجنب الترجمة إذا كان النص فارغًا
        
        english_words = re.findall(r'\b[A-Za-z0-9-]+\b', text)
        translated_text = GoogleTranslator(source='en', target='ar').translate(text)

        for word in english_words:
            translated_text = re.sub(r'\b' + re.escape(word) + r'\b', word, translated_text)

        return translated_text
    except Exception as e:
        print(f"⚠️ خطأ أثناء الترجمة: {e}")
        return text

@client.on(events.NewMessage(chats=source_channels))
async def my_event_handler(event):
    try:
        original_text = event.message.text
        media = event.message.media  # التحقق مما إذا كان هناك صورة أو فيديو

        print(f"📥 رسالة مستلمة: {original_text[:50] if original_text else '[وسائط فقط]'}...")  # تتبع الرسائل المستلمة
        
        processed_text = clean_text(original_text)  # تنظيف النص
        translated_text = translate_text(processed_text)  # ترجمة النص
        final_message = f"{translated_text}\n\n{hashtags}" if translated_text else hashtags  # إضافة الهاشتاجات
        
        # التحقق مما إذا كان media عبارة عن WebPage Preview
        if isinstance(media, MessageMediaWebPage):
            print("⚠️ المحتوى يحتوي على معاينة ويب فقط، سيتم إرسال النص فقط بدون صورة.")
            media = None  # منع الإرسال كملف

        # إرسال الرسالة مع الصورة أو الفيديو إن وجد
        if isinstance(media, (MessageMediaPhoto, MessageMediaDocument)):  # دعم الصور والفيديوهات
            await client.send_file(destination_channel, media, caption=final_message, parse_mode="Markdown")
        else:
            await client.send_message(destination_channel, final_message, parse_mode="Markdown")

        print(f"✅ تم نشر الرسالة: {translated_text[:50] if translated_text else '[وسائط فقط]'}...")
    
    except Exception as e:
        print(f"⚠️ خطأ أثناء المعالجة: {e}")

# تشغيل العميل
try:
    client.start()
    client.run_until_disconnected()
except Exception as e:
    print(f"❌ فشل تشغيل البوت: {e}")
#  Coded By MDLeet
