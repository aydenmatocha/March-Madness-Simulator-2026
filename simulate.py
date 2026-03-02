from teams import team_ratings
from bracket import region1
import random

def main():
    sim_round1()
    pass

def strip_seed(team_name):
    return team_name.split(" ", 1)[1]

# Basic simulation, will change later
def sim_game(team1, team2):
    team1ns = strip_seed(team1)
    team2ns = strip_seed(team2)
    r1 = team_ratings[team1ns]
    r2 = team_ratings[team2ns]

    prob_team1 = r1 / (r1 + r2)

    return team1 if random.random() < prob_team1 else team2

def sim_round1():
    print("ROUND 1:")
    # Region 1
    print("Region 1:")
    region1winners = []
    for team1, team2 in region1:
        winner = sim_game(team1, team2)
        region1winners.append(winner)
    print(region1winners)

    # Region 2

    # Region 3

    # Region 4
    pass
    

if __name__ == "__main__":
    main()