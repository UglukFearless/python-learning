import requests

url = 'http://example.com'
r = requests.get(url)
print(r.text)

params = { 'key1': 'value1', 'key2': 'value2' }
r = requests.get(url, params=params)
print(r.url)

url = 'http://httpbin.org/cookies'
cookies = { 'cookies_are': 'working' }
r = requests.get(url, cookies=cookies)
print(r.text)

print(r.cookies)