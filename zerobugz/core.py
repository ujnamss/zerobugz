import os
import json
import requests

api_key = os.getenv("ZB_API_KEY", "default")
serverBaseUrl = os.getenv("ZB_SERVER_BASE_URL", "https://0bugz.com/api")
headers = {
    'Content-type': "application/json"
}

def load_test_cases(schema, count):
    variationsPayload = None
    with open(schema) as json_data:
        variationsPayload = json.load(json_data)

    variations = []
    if variationsPayload:
        # Add retry logic
        variationsAPIUrl = "{}/variations".format(serverBaseUrl)
        variationsAPIUrl = "{}?count={}".format(variationsAPIUrl, count)
        variationsResponse = requests.post(variationsAPIUrl, headers=headers, data=json.dumps(variationsPayload))
        if variationsResponse.status_code < 200 or variationsResponse.status_code > 300:
            variationsResponse = json.loads(variationsResponse.text)
            assert(variationsResponse["status"] == 'failure')
            print("zerobugz: data generation failed: {}".format(variationsResponse["result"]))
        else:
            results = json.loads(variationsResponse.text)['result']
            assert(len(results) == count)
            for result in results:
                variations.append((result, ))
    return variations
