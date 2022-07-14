import datetime
import time


istBufferInSeconds = +(((5 * 60) + 30) * 60)

def printLog(log):
	nowDateAndTime = datetime.datetime.fromtimestamp(time.time()
	                                                    + istBufferInSeconds).strftime('%a %b %d %Y | %I:%M:%S.%f %p')
	nowDateAndTime = nowDateAndTime[:-6] + nowDateAndTime[-3:]
	printStatement = ("\n["
	                  + nowDateAndTime
	                  + " IST]\t"
	                  + str(log))
	print(printStatement)
	return printStatement
