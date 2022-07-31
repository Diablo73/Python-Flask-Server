import json


# @app.route("/json/minify/<jsonArg>", methods=['GET'])
def jsonMinify(jsonArg):
	try:
		return "<pre>" + json.dumps(json.loads(jsonArg), separators=(',', ':')) + "</pre>"
	except Exception as e:
		return jsonArg + "\n\n❌" + str(e)

# @app.route("/json/beautify/<jsonArg>", methods=['GET'])
def jsonBeautify(jsonArg):
	try:
		return "<pre>" + json.dumps(json.loads(jsonArg), indent=4).replace("    ", "&#9;") + "</pre>"
	except Exception as e:
		return jsonArg + "\n\n❌" + str(e)
