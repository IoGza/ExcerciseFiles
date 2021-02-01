winners = open("WorldSeriesWinners.txt", "r")


teamWinners = {}

# userYear = int(input("Input the year of the team that won: "))
count = 1903
for team in winners:
    teamWinners[team] = count
    count +=1 
    print(teamWinners)

    
    
