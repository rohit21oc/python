game_played = int(input("Enter how many game u played: "))
game_won = int(input("Enter how many game u won: "))
game_lost = int(input("Enter how many game u lost: "))
game_tie = game_played - game_won- game_lost;

total_points = game_won * 4+ game_tie*2;
print(f"Your total points are {total_points}")