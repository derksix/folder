import telebot
from telebot import types

 
bot = telebot.TeleBot('1162401802:AAGgvCoju5jxeTwNDXzr2vBOP36t_V6yevA')
 
@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    qiwi_button = types.InlineKeyboardButton(text="Оплатить QIWI", url="https://qiwi.com/n/AGOVI674")
    
    keyboard.add(qiwi_button)
    bot.send_message(message.chat.id, """*Сбор денег на обновление моего ноутбука*
        \n*Организатор*: _Петр Грыцко_, Украина
        \nЦель: 2000₽
        \n*Характеристики*:\nLenovo b590 2012 года\nIntel Celeron b830 1.8 Мг\nОЗУ 2 гб\nбез видеокарты\nос WINDOWS 10 x32 (_очень сильно лагает_)
        \n*Я хочу обновить ОЗУ до 8 гб*\nПереведите мне хотя бы 5 рублей\n_Ведь это так мало для вас но очень много для меня_
        \n*Мои реквизиты*:\n*BTC* - `37SVLeQP6GSuguVpfbfiwMxKXoTM3bVNLt`\n*ETH* - `0xd2416184C8EA7fe06865ff0AdBA434f2F6eEB0E4`""", reply_markup=keyboard, parse_mode='Markdown')

bot.polling(none_stop=True)