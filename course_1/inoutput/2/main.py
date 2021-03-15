def calcWords(d, inputString):
    words = inputString.split()
    for word in words:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1

def getPopularWord(d):
    result = -1
    for k,v in d.items():
        if result == -1:
            result = k
        elif v > d[result]:
            result = k
        elif v == d[result] and k < result:
            result = k
    return result

with open('.\course_1\inoutput\\2\input.txt', 'r') as data:
    result = ''
    d = {}
    lines = data.read().splitlines()
    for line in lines:
        line = line.strip().lower()
        calcWords(d, line)

    word = getPopularWord(d)

    result = word + ' ' + str(d[word])

    with open('.\course_1\inoutput\\2\output.txt', 'w') as res:
        res.write(result)