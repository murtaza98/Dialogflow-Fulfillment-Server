from flask import Flask, request
import requests

app = Flask(__name__)

incoming_endpoint_url = 'http://localhost:3000/api/apps/public/783d8e4d-b06a-409a-aaf3-b37650dc0a26/incoming'
fulfillment_endpoint_url = 'http://localhost:3000/api/apps/public/783d8e4d-b06a-409a-aaf3-b37650dc0a26/fulfillments-endpoint'


@app.route('/', methods=['GET', 'POST'])
def fulfillment_server():
	print(request.json)

	response_fulfillment = requests.post(url=fulfillment_endpoint_url, json=request.json)
	print('Successfully sent the fulfillment message to app. Its response', response_fulfillment)

	session = request.json['session'].split('/')[-1]
	intent_name = request.json['queryResult']['intent']['displayName']

	print('Fulfillment request received, Intent->', intent_name, '  session->', session)

	if intent_name == 'support.livechat':
		request_data = {
			'action': 'handover',
			'sessionId': session
		}
		response = requests.post(url=incoming_endpoint_url, data=request_data)
		print('Response from incominf endpoint', response)
	elif intent_name == 'coronavirus.confirmed_cases':
		return {
				"fulfillmentMessages": [
					{
						"text": {
							"text": [
								"About 3 million"
							]
						}
					}
				]
			}
	return '''{}'''


if __name__ == '__main__':
	app.run(port=4000, debug=True)
