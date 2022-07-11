import os, time
import utils, flipkart
import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


def start(update: Update, context: CallbackContext):
	utils.printLog(update)
	update.message.reply_text("Hello " + update.message.chat.first_name + ", Welcome to E-Commerce Tracker Bot.\n" +
	                          "This bot tracks the availablity of a product at different e-commerce websites.\n" +
	                          "Please write /help to see its usage.")


def help(update: Update, context: CallbackContext):
	utils.printLog(update.message.chat.first_name + " wants help!!!")
	update.message.reply_text("Just share and paste the product link here. The bot'll take care of the rest." +
	                          "Currently supported websites -\n" +
	                          "1. <a href=\"https://www.flipkart.com/\">Flipkart</a>",
	                          parse_mode=telegram.constants.PARSEMODE_HTML, disable_web_page_preview=True)


def unknown(update: Update, context: CallbackContext):
	utils.printLog(update.message.chat.first_name + " has gone crazy!!!")
	update.message.reply_text("You need /help!!!!!")


def sendMsg(update, message):
	utils.printLog(update.message.chat.first_name + " reply sent!!!")
	messageId = update.message.message_id
	update.message.reply_text(message, parse_mode=telegram.constants.PARSEMODE_HTML, disable_web_page_preview=True,
	                          reply_to_message_id=messageId)


def sharedUrl(update: Update, context: CallbackContext):
	url = update.message.text
	utils.printLog(update.message.chat.first_name + " wants to track -> " + url)
	inStock = False
	firstHit = True
	startTime = time.time()
	endTime = time.time()

	while not inStock and time.time() - startTime < 3600:
		if "flipkart" in url:
			inStock, message = flipkart.goToFlipkart(update, url)
			if firstHit and not inStock:
				firstHit = False
				notInStockMsg = flipkart.getFlipkartNotInStockMsg(url)
				sendMsg(update, notInStockMsg + "\n<b>WILL KEEP CHECKING.......</b>")
		elif "amazon" in url:
			pass
		sleepTime = 5 - (time.time() - endTime)
		time.sleep(0 if sleepTime < 0 else sleepTime)
		endTime = time.time()

	if not inStock:
		message = notInStockMsg.replace("⚠️", "❌")

	sendMsg(update, message)


def startTelegramBot():
	result = ""
	try:
		utils.printLog("Initiating the telegram bot sequence!!! ⚠")
		updater = Updater(os.getenv("TELEGRAM_APP_API_TOKEN"), use_context=True)
		updater.stop()
		updater.dispatcher.add_handler(CommandHandler('start', start))
		updater.dispatcher.add_handler(CommandHandler('help', help))
		updater.dispatcher.add_handler(MessageHandler(Filters.entity('url'), sharedUrl, run_async=True))
		updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
		updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
		updater.start_polling()
		result = "The telegram bot has successfully RESTARTED!!! ✅✅✅"
		utils.printLog(result)
	except Exception as e:
		result = str(e) + " ❌❌❌"
		utils.printLog(result)
	finally:
		return result
