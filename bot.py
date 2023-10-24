import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Я устал....")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def guess_namber (update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0 ])
            message = f"Вы ввели число {user_number}"
        except  (TypeError, ValueError) :  
            message = "Введите целое число!!!"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)
   
def main():
    mybot = Updater(settings.API_KEY, use_context=True,)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_namber))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ =="__main__":
 main()
