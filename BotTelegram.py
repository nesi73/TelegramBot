from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import numpy as np
from os import remove

tablero = np.zeros(0)
barcosDisponibles = 6
barco3 = 1
barco2 = 2
barco1 = 3
primeraIteración = 0
upg = 0

def start(bot, update):
  """ This function will be executed when '/start' command is received """
  message = "Welcome to the coolest bot ever!"
  bot.send_message(chat_id=update.message.chat_id, text=message)

def hello(bot, update):
  """ This function will be executed when '/hello' command is received """
  greeting = "Hi there, {}".format(update.effective_user.username)
  bot.send_message(chat_id=update.message.chat_id, text=greeting)
def button(bot, update):
  query = update.callback_query
  f = open('pbSolucion.txt','r')
  cont = 1
  global tablero
  a = np.zeros(0)
  for l in f:
    b = [str(l[0]),str(l[2]),str(l[4]),str(l[6]),str(l[8]),
    str(l[10]),str(l[12]),str(l[14])]
    a = np.append(a,b)
  ind = query.data
  if a[int(query.data)] == '1':
    msg = 'tocado'
    bot.edit_message_text(text=msg,chat_id=query.message.chat_id,message_id=query.message.message_id)
    solucionTablero = 
    tablero[int(query.data)] = '1'
    if(int(query.data) == 0):
      tablero[int(query.data) + 9] = '*'
    elif(int(query.data) == 56):
      tablero[int(query.data) - 7] = '*'
    elif(int(query.data) == 7):
      tablero[int(query.data) + 7] = '*'
    elif(int(query.data) == 63):
      tablero[int(query.data) - 9] = '*'
    elif(int(query.data)%8 == 0): #me están dando uno de la parte izquierda
      tablero[int(query.data) - 7] = '*'
      tablero[int(query.data) + 9] = '*'
    elif((int(query.data) +1)%8 == 0): #parte derecha
      tablero[int(query.data) - 9] = '*'
      tablero[int(query.data) + 7] = '*'
    elif ((int(query.data) < 7)): #parte de arriba
      tablero[int(query.data) + 7] = '*'
      tablero[int(query.data) + 9] = '*'
    elif (int(query.data) > 56): #parte de abajo
      tablero[int(query.data) - 7] = '*'
      tablero[int(query.data) - 9] = '*'
    else:
      tablero[int(query.data) - 7] = '*'
      tablero[int(query.data) - 9] = '*'
      tablero[int(query.data) + 7] = '*'
      tablero[int(query.data) + 9] = '*'
  else:
    msg = 'agua'
    bot.edit_message_text(text=msg,chat_id=query.message.chat_id,message_id=query.message.message_id)
    tablero[int(query.data)] = '*'
  cont = 0
  f.close()
  remove('pb.txt')
  f = open('pb.txt','w')
  for i in range(8):
    for t in range(8):
      f.write(str(tablero[cont]))
      f.write(" ")
      cont = cont + 1
    f.write("\n")
  f.close()
  mostrarTablero()

def mostrarTablero():
  f = open('pb.txt','r')
  cont = 0
  global tablero
  a = np.zeros(0)
  for l in f:
    b = [InlineKeyboardButton(str(l[0]), callback_data=str(cont)),
    InlineKeyboardButton(str(l[2]), callback_data=str(cont+1)),
    InlineKeyboardButton(str(l[4]), callback_data=str(cont+2)),
    InlineKeyboardButton(str(l[6]), callback_data=str(cont+3)),
    InlineKeyboardButton(str(l[8]), callback_data=str(cont+4)),
    InlineKeyboardButton(str(l[10]), callback_data=str(cont+5)),
    InlineKeyboardButton(str(l[12]), callback_data=str(cont+6)),
    InlineKeyboardButton(str(l[14]), callback_data=str(cont+7))]
    u = [str(l[0]),str(l[2]),str(l[4]),str(l[6]),str(l[8]),str(l[10]),str(l[12]),str(l[14])]
    a = np.append(a,b)
    tablero = np.append(tablero,u)
    cont = cont + 8
  a = np.reshape(a,(8,8))
  reply_markup = InlineKeyboardMarkup(a)
  upg.message.reply_text('Elige el servicio:',reply_markup=reply_markup)
  f.close()

def info(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text ="¿Serás capaz de derrotarme?")
  global upg
  upg = update
  mostrarTablero()


def add(bot, update, args):
  """ This function will be executed when '/add arg1, arg2, ...' command is received """

  # First converts the string list to a int list and then add all the elems
  result = sum(map(int, args))
  message = "The result is: {}".format(result)
  bot.send_message(chat_id=update.message.chat_id, text=message)

def main(bot_token):
  """ Main function of the bot """
  updater = Updater(token=bot_token,)
  dispatcher = updater.dispatcher

  # Command handlers
  start_handler = CommandHandler('start', start)
  hello_handler = CommandHandler('hello', hello)
  add_handler = CommandHandler('add', add, pass_args=True)
  info2_handler = CommandHandler('info', info)

  # Add the handlers to the bot
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(hello_handler)
  dispatcher.add_handler(add_handler)
  dispatcher.add_handler(info2_handler)
  dispatcher.add_handler(CallbackQueryHandler(button))


  # Starting the bot
  updater.start_polling(allowed_updates=[])
  
if __name__ == "__main__":
  TOKEN = "" #your token
  main(TOKEN)