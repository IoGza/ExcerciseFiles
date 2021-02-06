winnersList = open("WorldSeriesWinners.txt").read().splitlines()

teamWinners = {}
winFrequency = {}

count = 1903
teamCount = 0
userYear = int(input("Input the year of the team that won (1903 - 2008): "))


for team in winnersList:

    if count == 1904:
        count += 1
        teamWinners[1905] = 'New York Giants'

    elif count == 1994:
        count+=1
        teamWinners[1995] = 'Atlanta Braves'
    else:

        winFrequency[team] = winnersList.count(team)

        teamWinners[count] = winnersList[teamCount]

    count += 1

    teamCount += 1


print(teamWinners)


teamName = teamWinners.get(userYear)

if userYear == 1904 or userYear == 1994:
    print("The World Series was not played that year")
else:
    print(
        "The",
        teamWinners.get(userYear),
        "won the World Series that year for a total of",
        winFrequency.get(teamName),
        "time(s)",
    )
