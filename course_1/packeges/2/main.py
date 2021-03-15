import requests

file_url_default = 'https://example-files.online-convert.com/document/txt/example.txt'
file_url = 'https://stepic.org/media/attachments/course67/3.6.2/872.txt'

r = requests.get(file_url.strip())

print(len(r.text.splitlines()))