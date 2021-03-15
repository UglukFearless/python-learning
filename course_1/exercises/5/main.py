

heightsData = {}

for i in range(1, 12):
    heightsData[i] = []

with open('.\course_1\exercises\\5\input.tsv', 'r') as tsvfile:
    rows = tsvfile.read().splitlines()
    for row in rows:
        words = row.split()

        heightsData[int(words[0])].append(float(words[2]))


with open('.\course_1\exercises\\5\output.txt', 'w') as output:
    for yearStudy in heightsData.keys():
        heights = heightsData[yearStudy]
        res = '-'

        if len(heights) > 0:
            res = str(sum(heights)/len(heights))
        print(yearStudy, res)
        output.writelines(str(yearStudy) + ' ' + str(float(res)) + '\n')