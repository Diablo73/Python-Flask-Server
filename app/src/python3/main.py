import flask
import logging
import utils
from controllers import jsonControllers, telegramControllers


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
app = flask.Flask("Flask4Telegram")

app.add_url_rule("/json/minify/<jsonArg>", view_func=jsonControllers.jsonMinify)
app.add_url_rule("/json/beautify/<jsonArg>", view_func=jsonControllers.jsonBeautify)
app.add_url_rule("/telegramBot/<password>/refresh", view_func=telegramControllers.refresh)
app.add_url_rule("/telegramBot/<password>/shutdown", view_func=telegramControllers.shutdown)

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
