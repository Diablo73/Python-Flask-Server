import requests

FLIPKART_URL = "flipkart.com/"
CASHKARO_URL = "https://cashkaro.com/stores/flipkart?r=18172340&fname=Ashul%20Gupta"
FLIPKART_API_URL = "https://flipkart.dvishal485.workers.dev/product/min/"


def goToFlipkart(url):
	i = url.index(FLIPKART_URL) + len(FLIPKART_URL)
	response = requests.get(FLIPKART_API_URL + url[i:]).json()
	inStock = True if response["in_stock"] else False
	if not inStock:
		return False, ""
	name = response["name"]
	currentPrice = response["current_price"]
	originalPrice = response["original_price"]
	discounted = "✅" if response["discounted"] else "❌"
	discount = str(originalPrice - currentPrice) + " (" + str(response["discount_percent"]) + "%)"
	rating = response["rating"]
	inStockEmoji = "✅" if response["in_stock"] else "❌"
	fAssured = "✅" if response["f_assured"] else "❌"
	shareUrl = response["share_url"]

	message = "<b>" + name + "</b>" + """\n
	Price = Rs""" + str(currentPrice) + " <s>Rs" + str(originalPrice) + """</s>
	Discount = Rs""" + discount + " " + discounted + """
	In stock = """ + inStockEmoji + """
	Flipkart Assured = """ + fAssured + """
	Rating = """ + str(rating) + " ⭐" + """
	<a href=\"""" + CASHKARO_URL + """\">Click Here</a>"""
	return True, message

def getFlipkartNotInStockMsg(url):
	i = url.index(FLIPKART_URL) + len(FLIPKART_URL)
	response = requests.get(FLIPKART_API_URL + url[i:]).json()
	
	name = "<b><s>" + response["name"] + "</s></b>"
	currentPrice = response["current_price"]
	originalPrice = response["original_price"]
	
	return name + """\n
	Price = Rs""" + str(currentPrice) + " <s>Rs" + str(originalPrice) + """</s>
	In stock = """ + "⚠️ <b>NOT IN STOCK</b> ⚠️"