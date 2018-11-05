import os
import json
import requests
import threading

serverBaseUrl = os.getenv("ZB_SERVER_BASE_URL", "https://0bugz.com/api")
headers = {
    'Content-type': "application/json"
}

ctx = threading.local()

def load_test_cases(schema, count):
    headers['Authorization'] = os.getenv("ZB_API_KEY")
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
            json_resp = json.loads(variationsResponse.text)
            request_id = json_resp['request_id']
            assert(request_id != None)
            ctx.request_id = request_id
            print("zerobugz: request_id: {}".format(request_id))
            results = json_resp['result']
            assert(len(results) == count)
            for result in results:
                variations.append((result, ))
    return variations

def get_zb_request_id():
    return ctx.request_id

def set_expected_value(zb_request_id, zb_item_id, value):
    headers['Authorization'] = os.getenv("ZB_API_KEY")
    expected_value_api_url = "{}/expectedvalue".format(serverBaseUrl)
    payload = {
        'request_id': zb_request_id,
        'item_id': zb_item_id,
        'value': value
    }
    expected_value_resp = requests.post(expected_value_api_url, headers=headers, data=json.dumps(payload))
    json_resp = json.loads(expected_value_resp.text)
    if expected_value_resp.status_code < 200 or expected_value_resp.status_code > 300:
        assert(json_resp["status"] == 'failure')
        print("zerobugz: setting expectedvalue failed: {}".format(json_resp["result"]))
    else:
        assert(json_resp["status"] == 'success')
    return json_resp
