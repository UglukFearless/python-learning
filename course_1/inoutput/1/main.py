
with open('.\course_1\inoutput\\1\input.txt', 'r') as data:
    result = ''
    line = data.readline().strip()

    with open('.\course_1\inoutput\\1\output.txt', 'w') as res:
        last = ''
        numberStr = ''
        for letter in line:
            if (letter >= 'A'):
                if last != '':
                    result += last*int(numberStr)
                last = letter
                numberStr = ''
                continue
            else:
                numberStr += letter
        result += last*int(numberStr)    

        res.write(result)