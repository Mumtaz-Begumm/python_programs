from datetime import datetime, timedelta

def round_robin_schedule(teams, start_date):
    n = len(teams)
    matches = []
    match_days = {}
    match_day = start_date
    num_days = n - 1
    
    for day in range(num_days):
        match_days[day] = match_day
        for j in range(n // 2):
            match = (teams[j], teams[n - 1 - j])
            matches.append((match_day, match))
            match_day += timedelta(days=1)
        teams.insert(1, teams.pop())  # Rotate teams except the first one
        
    return matches, match_days

def single_elimination_schedule(teams, start_date):
    matches = []
    match_days = {}
    match_day = start_date
    num_teams = len(teams)
    num_rounds = num_teams - 1
    
    for i in range(num_rounds):
        match_days[i] = match_day
        for i in range(num_teams // 2):
            match = (teams[i], teams[num_teams - 1 - i])
            matches.append((match_day, match))
            match_day += timedelta(days=1)
        teams = teams[:num_teams // 2]  # Eliminate losing teams
        num_teams //= 2
        
    return matches, match_days

print("Select the sport [Cricket, Football, Chess]:")
sp = input()

print("Select number of teams [4-16]:")
nt = int(input())

teams = []
print("Enter the team names:")
for i in range(nt):
    team_name = input("Team {}: ".format(i + 1))
    teams.append(team_name)

start_date_str = input("Enter the starting date (YYYY-MM-DD): ")
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

# Initial round-robin scheduling
matches, match_days = round_robin_schedule(teams, start_date)

print("\nRound Robin Schedule:")
for match_day, match in matches:
    print("\nDay:", match_day.strftime("%Y-%m-%d"))
    print(match[0], "vs", match[1])

# Ask user to enter top 4 teams
print("\nEnter the top 4 teams:")
top_teams = []
for i in range(4):
    team_name = input("Team {}: ".format(i + 1))
    top_teams.append(team_name)

# Schedule playoffs for top 4 teams using single elimination
end_date = start_date + timedelta(days=75)  # 2.5 months is 75 days
playoff_matches_rank1_2, playoff_days_rank1_2 = single_elimination_schedule(top_teams[:2], end_date + timedelta(days=1))
playoff_matches_rank3_4, playoff_days_rank3_4 = single_elimination_schedule(top_teams[2:], end_date + timedelta(days=2))

print("\nPlayoff Schedule (Rank 1 vs Rank 2):")
for match_day, match in playoff_matches_rank1_2:
    print("\nDay:", match_day.strftime("%Y-%m-%d"))
    print(match[0], "vs", match[1])

print("\nPlayoff Schedule (Rank 3 vs Rank 4):")
for match_day, match in playoff_matches_rank3_4:
    print("\nDay:", match_day.strftime("%Y-%m-%d"))
    print(match[0], "vs", match[1])

# Prompt user to enter top 2 teams after playoffs
print("\nEnter the top 2 teams after playoffs:")
final_teams = []
for i in range(2):
    team_name = input("Team {}: ".format(i + 1))
    final_teams.append(team_name)

# Schedule final match
final_match_day = end_date + timedelta(days=max(len(playoff_matches_rank1_2), len(playoff_matches_rank3_4)))
print("\nFinal Match:")
print("Day:", final_match_day.strftime("%Y-%m-%d"))
print(final_teams[0], "vs", final_teams[1])