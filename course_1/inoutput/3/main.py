
with open('.\course_1\inoutput\\3\input.txt', 'r', encoding="utf8") as data:
    with open('.\course_1\inoutput\\3\output.txt', 'w') as res:
        
        count = 0
        mathSum = 0
        pthySum = 0
        RusSum = 0
        ratings = data.readline().strip().split(';')

        while ratings:
            print(ratings)
            if (len(ratings) == 4):
                middleRating = (float(ratings[1]) + float(ratings[2]) + float(ratings[3]))/3
                mathSum += float(ratings[1])
                pthySum += float(ratings[2])
                RusSum += float(ratings[3])
                count += 1
                res.write(str(middleRating) + '\n')
                ratings = data.readline().strip().split(';')
            else:
                ratings = False

        res.write(str(mathSum/count) + ' ' + str(pthySum/count) + ' ' + str(RusSum/count))