import requests as rq

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
    "authorization":" ",
    "message":"This is test message",
    "language":"english",
    "route":"q",
    "numbers":"9080888421"
    }

headers = {
    'cache-control': "no-cache"
}

response = rq.request("GET", url, headers=headers, params=querystring)

print(response.text)