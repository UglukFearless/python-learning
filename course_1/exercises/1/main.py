def checkTeamExist(teamName, allGames, wins, draws, looses, points):
    if not teamName in allGames.keys():
        allGames[teamName] = 0
        wins[teamName] = 0
        draws[teamName] = 0
        points[teamName] = 0
        looses[teamName] = 0


n = int(input())

allGames = {}
wins = {}
draws = {}
points = {}
looses = {}

count = 0
while count < n:
    count += 1
    gameData = input().split(';')
    team1 = gameData[0]
    goals1 = int(gameData[1])
    team2 = gameData[2]
    goals2 = int(gameData[3])

    checkTeamExist(team1, allGames, wins, draws, looses, points)
    checkTeamExist(team2, allGames, wins, draws, looses, points)

    allGames[team1] += 1
    allGames[team2] += 1

    if goals1 > goals2:
        wins[team1] += 1
        points[team1] += 3
        looses[team2] += 1
    elif goals1 == goals2:
        draws[team1] += 1
        points[team1] += 1
        draws[team2] += 1
        points[team2] += 1
    else:
        wins[team2] += 1
        points[team2] += 3
        looses[team1] += 1

for team in allGames.keys():
    first = team + ':' + str(allGames[team])
    print(first, wins[team], draws[team], looses[team], points[team])