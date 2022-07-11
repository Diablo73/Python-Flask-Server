import os
import flask
import waitress
import telegramBot, utils

app = flask.Flask("Flask4Telegram")

@app.route("/")
def start():
	result = "Flask server is live and RUNNING!!! ✅"
	utils.printLog(result)
	return result

@app.route("/refresh/<password>")
def refresh(password):
	if password == os.getenv("REFRESH_PASSWORD"):
		utils.printLog("The password is CORRECT!!! ✅")
		return telegramBot.startTelegramBot()
	else:
		result = "The password is WRONG!!! ❌"
		utils.printLog(result)
		return result


def main():
	try:
		utils.printLog("Initiating flask server!!! ⚠")
		waitress.serve(app, host="0.0.0.0", port=8080)
#		app.run(host='0.0.0.0', port=8080)
		utils.printLog("Flask server is live and RUNNING!!! ✅")
	except Exception as e:
		utils.printLog(e)


if __name__ == '__main__':
	main()
