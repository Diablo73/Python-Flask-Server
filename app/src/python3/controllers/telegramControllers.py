import os
import flask
# import waitress
import telegramBot
import utils


# @app.route("/telegramBot/<password>/refresh", methods=['GET'])
def refresh(password):
	if password == os.getenv("MASTER_PASSWORD"):
		result = utils.printLog("The password is CORRECT!!! ✅")
		return result + telegramBot.startTelegramBot()
	else:
		return utils.printLog("The password is WRONG!!! ❌")

# @app.route("/telegramBot/<password>/shutdown", methods=['GET'])
def shutdown(password):
	if password == os.getenv("MASTER_PASSWORD"):
		result = utils.printLog("The password is CORRECT!!! ✅")
		shutdown_func = flask.request.environ.get("werkzeug.server.shutdown")
		werkzeug = "Not running werkzeug!!! ❌"
		if shutdown_func is not None:
			werkzeug = "Flask werkzeug server is SHUTTING DOWN!!! ✅"
			shutdown_func()
		result += utils.printLog(werkzeug)
		return result
	else:
		return utils.printLog("The password is WRONG!!! ❌")
