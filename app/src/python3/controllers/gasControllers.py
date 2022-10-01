import os
import utils
import restAPI


# @app.route("/links/<password>/<method>/<otp>", methods=['GET'])
def links(password, method, otp):
	if password == os.getenv("MASTER_PASSWORD"):
		result = utils.printLog("The password is CORRECT!!! ✅")
		response = restAPI.post(os.getenv("WEB_APP_URL"), {"password": password, "otp": otp, "method": method})
		return result + utils.printLog(response)
	else:
		return utils.printLog("The password is WRONG!!! ❌")
