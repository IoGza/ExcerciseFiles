winnersList = open("WorldSeriesWinners.txt").read().splitlines()

teamWinners = {}
winFrequency = {}

userYear = int(input("Input the year of the team that won (1903 - 2009): "))
count = 1903
teamCount = 0


for team in winnersList:

    # if count != 1904 or count != 1994:

    winFrequency[team] = winnersList.count(team)
    count += 1
    
    teamWinners[count] = winnersList[teamCount]
    teamCount += 1
    
    

teamName = teamWinners.get(userYear)
print(teamWinners.get(userYear))
print(winFrequency.get(teamName))


# print(teamWinners)
# print(winFrequency)
