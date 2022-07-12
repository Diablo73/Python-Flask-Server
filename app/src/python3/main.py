import os
import flask
# import waitress
import logging
import telegramBot, utils


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
app = flask.Flask("Flask4Telegram")

@app.route("/")
def start():
	result = "Flask server is live and RUNNING!!! ✅"
	utils.printLog(result)
	return result

@app.route("/refresh/<password>")
def refresh(password):
	if password == os.getenv("MASTER_PASSWORD"):
		utils.printLog("The password is CORRECT!!! ✅")
		return telegramBot.startTelegramBot()
	else:
		result = "The password is WRONG!!! ❌"
		utils.printLog(result)
		return result

@app.route("/shutdown/<password>")
def shutdown(password):
	if password == os.getenv("MASTER_PASSWORD"):
		utils.printLog("The password is CORRECT!!! ✅")
		shutdown_func = flask.request.environ.get("werkzeug.server.shutdown")
		result = "Not running werkzeug!!! ❌"
		if shutdown_func is not None:
			result = "Flask werkzeug server is SHUTTING DOWN!!! ✅"
			shutdown_func()
		utils.printLog(result)
		return result
	else:
		result = "The password is WRONG!!! ❌"
		utils.printLog(result)
		return result


def main():
	try:
		utils.printLog("Initiating flask server!!! ⚠")
#       waitress.serve(app, host="0.0.0.0", port=8080)
		app.run(host='0.0.0.0', threaded=True, port=8080)
		utils.printLog("Flask server is live and RUNNING!!! ✅")
	except Exception as e:
		utils.printLog(e)


if __name__ == '__main__':
	main()
