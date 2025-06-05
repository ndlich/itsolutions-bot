
import telebot
import os

# Вставь сюда свой токен
TOKEN = "7808918715:AAFlnQL615HPTBf046w-B3v3mXqMTe6zB_C"
# ID владельца, кому пересылать заявки
OWNER_ID = 7820814910

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text", "photo", "audio", "document", "video", "voice", "video_note"])
def forward_message(message):
    try:
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "✅ Спасибо! Заявка отправлена. Я скоро с тобой свяжусь.")
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Что-то пошло не так. Попробуй позже.")
        bot.send_message(OWNER_ID, f"Ошибка пересылки сообщения: {e}")

@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id,
        "👋 Привет!\n"
        "Я помогу понять, почему тормозит твой компьютер.\n"
        "Пришли, пожалуйста:\n"
        "- 📷 скриншот (автозагрузка или диспетчер задач)\n"
        "- ✍️ или короткое описание проблемы\n\n"
        "Можно также отправить голосовое, файл или видео."
    )

bot.polling(none_stop=True)
