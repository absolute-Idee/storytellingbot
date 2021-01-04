import config 
import story as s
import telebot
#from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

count=0
bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])
def inrto(message):
    bot.send_message(message.chat.id, "У этого бота для тебя есть рассказ. Он разбит на части, так что запусти его словами: часть 1(если он остановился, пора переходить на другую часть)", parse_mode='html')
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, s.strings[3], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[5], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[6], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[7], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[8], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[9], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[10], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[11], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[12], parse_mode='html')
                
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, s.strings[4], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[5], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[6], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[8], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[9], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[10], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[11], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[12], parse_mode='html')
            elif call.data =='managecall':
                bot.send_message(call.message.chat.id, s.strings[19], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[20], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[21], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[22], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[23], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[24], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[25], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[26], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[27], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[28], parse_mode='html')
            elif call.data =='window':
                bot.send_message(call.message.chat.id, s.strings[42], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[43], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[44], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[45], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[46], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[47], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[48], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[49], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[50], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[51], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[52], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[53], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[54], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[55], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[56], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[57], parse_mode='html')
                bot.send_message(call.message.chat.id, s.strings[58], parse_mode='html')
                
                
                
    except Exception as e:
        print(repr(e))            




@bot.message_handler(content_types=['text'])
def part2(message):
    if message.text=="часть 1" or message.text=="Часть 1":
        bot.send_message(message.chat.id, s.strings[0], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[1], parse_mode='html')

        markup=types.InlineKeyboardMarkup(row_width=2)
        item1=types.InlineKeyboardButton("Встать с кровати",callback_data='good')
        item2=types.InlineKeyboardButton("Поспать 5 минут", callback_data='bad')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, s.strings[2], parse_mode='html', reply_markup=markup)

    if message.text=="часть 2" or message.text=="Часть 2":
        bot.send_message(message.chat.id, s.strings[13], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[14], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[15], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[16], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[17], parse_mode='html')      

        markup=types.InlineKeyboardMarkup(row_width=2)
        item3=types.InlineKeyboardButton("Позвонить менеджеру",callback_data='managecall')
        markup.add(item3)

        bot.send_message(message.chat.id, s.strings[18], parse_mode='html', reply_markup=markup)

    if message.text=='часть 3' or message.text=="Часть 3":
        bot.send_message(message.chat.id, s.strings[29], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[30], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[31], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[32], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[33], parse_mode='html')  
        bot.send_message(message.chat.id, s.strings[34], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[35], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[36], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[37], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[38], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[39], parse_mode='html')
        bot.send_message(message.chat.id, s.strings[40], parse_mode='html')

    if message.text=='часть 4'or message.text=="Часть 4":
        
        markup=types.InlineKeyboardMarkup(row_width=2)
        item4=types.InlineKeyboardButton("Следующее видео",callback_data='manag')
        item5=types.InlineKeyboardButton("Подойти к окну",callback_data='window')
        markup.add(item4,item5)

        bot.send_message(message.chat.id, s.strings[41], parse_mode='html', reply_markup=markup)

         

        


bot.polling(none_stop=True)
