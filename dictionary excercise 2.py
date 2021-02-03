winnersList = open("WorldSeriesWinners.txt").read().splitlines()

teamWinners = {}
winFrequency = {}

count = 1903
teamCount = 0
userYear = int(input("Input the year of the team that won (1903 - 2009): "))


for team in winnersList:
    
    if userYear == 1904 or userYear == 1994:
        print("The world series did not happen that year")
        break
    else:
        
        winFrequency[team] = winnersList.count(team)
        

        teamWinners[count] = winnersList[teamCount]
        teamCount += 1
        count += 1

     
teamName = teamWinners.get(userYear)
        
print("The",teamWinners.get(userYear), "won the World Series", winFrequency.get(teamName), "time(s)")




