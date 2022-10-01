import requests


def post(url, payload):
	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json"
	}
	response = requests.post(url, json=payload, headers=headers)
	return response.text
