import datetime
import time


def printLog(s):
	print("[" + datetime.datetime.fromtimestamp(time.time() + 19800).strftime('%a %b %d %Y | %H:%M:%S.%f') + "]", end="\t")
	print(s)
