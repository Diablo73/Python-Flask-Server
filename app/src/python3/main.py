import os
import flask
# import waitress
import logging
import telegramBot, utils


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
app = flask.Flask("Flask4Telegram")

@app.before_request
def before_request_callback():
	pass

@app.after_request
def after_request_callback(response):
	response.data = response.data.decode('utf-8').replace("\n", "<br>").replace("\t", "&emsp;").encode('utf-8')
	return response

@app.route("/")
def start():
	return utils.printLog("Flask server is live and RUNNING!!! ✅")

@app.route("/refresh/<password>")
def refresh(password):
	if password == os.getenv("MASTER_PASSWORD"):
		result = utils.printLog("The password is CORRECT!!! ✅")
		return result + telegramBot.startTelegramBot()
	else:
		return utils.printLog("The password is WRONG!!! ❌")

@app.route("/shutdown/<password>")
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
