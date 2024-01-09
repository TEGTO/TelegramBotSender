import telebot
from telebot import types
from messageInfo import messageInfo
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta, time

scheduler = BackgroundScheduler()
scheduler.start()

SEND_MESSAGE = "Send Message"
SEND_DELAYED_MESSAGE = "Send Delayed Message"
SET_MESSAGE_CONTENT = "Set Message Content"
SPLIT_SYMBOL = "$"
controller_id = 0 # if you want the bot to be controlled only by a specific id

botTocken = ""
bot = telebot.TeleBot(botTocken)
messageContent = ""

def initialize_sender_bot():
    global allowed_group_id
    bot.infinity_polling(none_stop=True)

@bot.message_handler(commands=['start', 'help'])
def _start(message):
    _interaction_buttons(message)

@bot.message_handler(func=lambda message: True)
def _handle_all_messages(message):
    #if(message.chat.id == controller_id):
    if(message.chat.type == "private"):
        if message.text == SEND_MESSAGE:
            _send_message(message)
        elif message.text == SEND_DELAYED_MESSAGE:
             _send_delayed_message(message)
        elif message.text == SET_MESSAGE_CONTENT:
            _set_message(message)
        else: 
            photo = open("what.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
    
def _send_message(message):
    send_text_message(bot, message.chat.id, "So, shall we start...")
    send_text_message(bot, message.chat.id, "Use this format to send your message:")
    send_text_message(bot, message.chat.id, f"Chat Id{SPLIT_SYMBOL}Amount of messages")
    bot.register_next_step_handler(message, _process_given_info_send_message)

def _send_delayed_message(message):
    send_text_message(bot, message.chat.id, "So, shall we start...")
    send_text_message(bot, message.chat.id, "Use this format to send your message, the delayed message will send at the same time every day:")
    send_text_message(bot, message.chat.id, f"Chat Id{SPLIT_SYMBOL}Amount of messages{SPLIT_SYMBOL}11:20{SPLIT_SYMBOL}Amount of days")
    bot.register_next_step_handler(message, _process_given_info_send_message_delayed)

def _set_message(message):
    send_text_message(bot, message.chat.id, "Send in next message to me, what you want to put in your message.")
    bot.register_next_step_handler(message, _process_given_message)

def _interaction_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    setMessage = types.KeyboardButton(SET_MESSAGE_CONTENT)
    sendMessage = types.KeyboardButton(SEND_MESSAGE)
    sendDelayedMessage = types.KeyboardButton(SEND_DELAYED_MESSAGE)
    markup.add(setMessage,sendMessage, sendDelayedMessage)
    bot.reply_to(message, text="Hello! I'm Joe Biden and today we will give a lesson to some naughty kids.", reply_markup = markup)

def _process_given_info_send_message(message):
    try:
        info = message.text.split({SPLIT_SYMBOL})
        message_info = messageInfo(info[0].strip(), int(info[1].strip()), "None", "None")
        _send_message_content(message_info)
    except Exception as e:
        send_text_message(bot, message.chat.id, f"An error occurred: {str(e)}")

def _process_given_info_send_message_delayed(message):
    try:
        info = message.text.split({SPLIT_SYMBOL})
        message_info = messageInfo(info[0].strip(), int(info[1].strip()), info[2].strip(), int(info[3].strip()))
        send_time = message_info.sendTime.split(":")
        if len(send_time) == 1:
            send_time.append("00")
        given_time = time(int(send_time[0]), int(send_time[1]))
        current_date = datetime.now().date()
        combined_datetime = datetime.combine(current_date, given_time)
        send_text_message(bot, message.chat.id, "Message is set")
        end_date = combined_datetime + timedelta(days=message_info.amountOfDays - 1)
        scheduler.add_job(_send_message_content, 'interval', hours=24, start_date=combined_datetime,
                          args=[message_info], end_date=end_date)
    except Exception as e:
       send_text_message(bot, message.chat.id, f"An error occurred: {str(e)}")

def _process_given_message(message):
    try:
        global messageContent
        messageContent = message
        send_text_message(bot, message.chat.id, "Message content is set")
    except Exception as e:
        send_text_message(bot, message.chat.id, f"An error occurred: {str(e)}")

def _send_message_content(kill_spam_message_info):
        chatId = int(kill_spam_message_info.chatId)
        for x in range(0, kill_spam_message_info.amountOfMessages):
            if messageContent.text:
                send_text_message(bot, chatId, messageContent.text)
            elif messageContent.photo:
             bot.send_photo(chatId, messageContent.photo[-1].file_id)
            elif messageContent.video:
                bot.send_video(chatId, messageContent.video.file_id)
         
def send_text_message(bot, chat_id, text):
    bot.send_message(chat_id, text)