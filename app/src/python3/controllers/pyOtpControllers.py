import time
import pyotp
from io import StringIO
from qrcode import QRCode


# @app.route("/2fa/generate/<secret>", methods=['GET'])
def generate(secret):
	try:
		otp = pyotp.TOTP(secret)
		auth_string = otp.provisioning_uri(name="pyOtp", issuer_name="Diablo73", )
		print(makeQRCodeMessage(auth_string, "text"))
		return "<pre style='text-align: center;'>" + makeQRCodeMessage(auth_string, None) + "</pre>"
	except Exception as e:
		return secret + "\n\n❌" + str(e)


# @app.route("/2fa/validate/<secret>/<otp>", methods=['GET'])
def validate(secret, otp):
	try:
		if otp == pyotp.TOTP(secret).now() or pyotp.TOTP(secret).verify(otp, time.time() - 30):
			return "<pre>✅ TRUE ✅</pre>"
		else:
			return "<pre>❌ FALSE ❌</pre>"
	except Exception as e:
		return secret + "\n\n❌" + str(e)


def makeQRCode(data, invertParam):
	sio = StringIO()
	qr_code = QRCode()
	qr_code.add_data(data)
	qr_code.print_ascii(out=sio, invert=invertParam)
	return "\n".join(line.lstrip() for line in sio.getvalue().split("\n"))


def makeQRCodeMessage(data, invertParam):
	return "\n\n\n" + makeQRCode(data, invertParam) + "\n\n\ncontent: " + data
