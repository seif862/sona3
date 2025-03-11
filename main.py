from flask import Flask
from threading import Thread
import telebot

# التوكن الخاص بالبوت
TOKEN = '7848973581:AAE9Vd-3i8I0urRemro1QtLn7nqkimTlAds'
bot = telebot.TeleBot(TOKEN)

# الرسالة الترحيبية عند بدء المحادثة
WELCOME_MESSAGE = '''
مرحبًا! 🤝

نشكرك على رغبتك في دعم الجمعية الخيرية.

طرق التبرع المتاحة:
1. تحويل بنكي: [ضع بيانات الحساب البنكي هنا]
2. باي بال: [ضع رابط التبرع هنا]
3. زيارة مقر الجمعية: [ضع العنوان هنا]

للمزيد من التفاصيل، تواصل معنا على: [ضع رقم الهاتف أو البريد الإلكتروني هنا]
'''  

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, WELCOME_MESSAGE)

# إعداد السيرفر باستخدام Flask
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == '__main__':
    keep_alive()
    bot.infinity_polling()
