import os
import telebot
import yfinance as yf
from dotenv import load_dotenv

import HelpMessage
import get99co

load_dotenv()

API_KEY = os.getenv("API_KEY")
load_dotenv()
bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
  startMessage = HelpMessage.sendHelp()
  bot.send_message(message.chat.id, startMessage)

@bot.message_handler(commands=['get_99co'])
def get_99_co(message):
  listOfListings = get99co.scrape()
  sendListing(listOfListings, message)
  # bot.send_message(message.chat.id, listingMessage)
  
def sendListing(listOfListings, message):
  for list in listOfListings:
    bot.send_message(message.chat.id, str(list))


bot.infinity_polling()