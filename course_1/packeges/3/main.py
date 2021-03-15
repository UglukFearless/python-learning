import requests

prefix = 'https://stepic.org/media/attachments/course67/3.6.3/'
file_url = '699991.txt'

stop = False

count = 0
max_count = 1000
result = ''

logger = open('.\course_1\packeges\\3\log.txt', 'w')

while not stop:
    count += 1
    r = requests.get(prefix + file_url.strip())
    firstLine = r.text.splitlines()[0]
    firstWord = firstLine.split()[0]
    
    if firstWord == 'We' or count > max_count:
        stop = True
        result = r.text
    else:
        file_url = firstLine

    logger.write(str(count) + ' ' + file_url + '\n')
    print(str(count) + ' ' + file_url + '\n')

if count <= max_count:
    with open('.\course_1\packeges\\3\output.txt', 'w') as res:
        res.write(result)
        print(result)
else:
    print('Ошибка - переполнение')

logger.close()