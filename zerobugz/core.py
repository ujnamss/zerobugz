import os
import json
import requests

serverBaseUrl = "http://0bugz.com/api"
variationsAPIUrl = "{}/variations".format(serverBaseUrl)
headers = {
    'Content-type': "application/json"
}

# verify=False,
def load_test_cases(schema, count):
    variationsPayload = None
    with open(schema) as json_data:
        variationsPayload = json.load(json_data)

    if variationsPayload:
        variationsResponse = requests.post(variationsAPIUrl, headers=headers, data=json.dumps(variationsPayload))
        assert(variationsResponse.status_code >= 200 and variationsResponse.status_code <= 300)
        # print(variationsResponse.text)
        results = json.loads(variationsResponse.text)['result']
        assert(len(results) == count)
        variations = []
        for result in results:
            variations.append((result, ))
        return variations
    return None
