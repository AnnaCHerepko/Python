import requests
import json
import telebot
from telebot import TeleBot
 
TOKEN = "здесь любой токен"
 
bot: TeleBot = telebot.TeleBot(TOKEN)
 
Mydict = {
    "/eur": "EUR",
    "/usd": "USD",
    "/rub": "RUB",
}
 
class ConvertionException(Exception):
    pass
 
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Валютные операции /conversion'
    bot.reply_to(message,text)

@bot.message_handler(commands=['conversion'])
def operations(message: telebot.types.Message):
    text = 'Актуальные курсы:\n  /pln_to_usd \n  /pln_to_rub \n  /pln_to_eur \n  /usd_to_pln \n  /rub_to_pln \n  /eur_to_pln'
    r1 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/')  
    texts1 = json.loads(r1.content)  
    Rates1 = texts1.get('rates')  
    EUR1 = str(Rates1[0].get('mid'))
    r2 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/')  
    texts2 = json.loads(r2.content)  
    Rates2 = texts2.get('rates')  
    USD1 = str(Rates2[0].get('mid'))
 
    r3 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/rub/')  
    texts3 = json.loads(r3.content)  
    Rates3 = texts3.get('rates')  
    RUB1 = str(Rates3[0].get('mid'))
    Mydict = {'eur': '', 'usd': '', 'rub': '',}
    Mydict['eur'] = EUR1
    Mydict['usd'] = USD1
    Mydict['rub'] = RUB1
    for key in Mydict.keys():
        text = '\n'.join((text, key, '->', Mydict[key]))
    bot.reply_to(message, text)
 
@bot.message_handler(commands=['pln_to_usd'])
def pln_to_usd(message):
    bot.send_message(message.chat.id, 'Введите количесто pln,которые вы хотите конвертировать в usd')
    @bot.message_handler(content_types=['text',])
    def plnusd(message):
        r = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/') 
        texts = json.loads(r.content) 
        Rates = texts.get('rates')  
        USD = Rates[0].get('mid') 
        amount = int(message.text) 
        total = round((amount/USD),2) 
        result = f'{amount} pln это {total} usd' 
        if type(amount) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
 
        bot.send_message(message.chat.id, result)
 
 
@bot.message_handler(commands=['pln_to_rub'])
def pln_to_rub(message):
    bot.send_message(message.chat.id, 'Введите количесто pln,которые вы хотите конвертировать в rub: ')
    @bot.message_handler(content_types=['text', ])
    def plnrub(message):
        r4 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/rub/') 
        texts4 = json.loads(r4.content)  
        Rates4 = texts4.get('rates')  
        RUB4 = Rates4[0].get('mid')
        amount4 = int(message.text)
        total4 = round((amount4/RUB4),2)
        result4 = f'{amount4} pln это {total4} rub'
        bot.send_message(message.chat.id, result4)
 
 
bot.polling(none_stop=True)