# MiniGolf
user_name = input("Welcome to GC mini golf! What is your name? ")
game = input("Hi " + user_name + "! Would you like to play 3 hole or 6 holes today? ")
hole = int(game)
if hole == 3:
    hole1 = int(input("How many putts for hole 1? (par is 3) "))
    hole2 = int(input("How many putts for hole 2? (par is 3) "))
    hole3 = int(input("How many putts for hole 3? (par is 3) "))
    total = [hole1, hole2, hole3]
    score = 0
    score = sum(total, start=score)
    game_score = score - 9
    if game_score > 0:
        print(f"Nice try, {user_name}... Your total score was + {game_score}")
    elif game_score < 0:
        print(f"Great Job, {user_name}! Your total score was {game_score}")
    else:
        print(f"Good game, {user_name}. Your total score was: 0")
else:
    hole1 = int(input("How many putts for hole 1? (par is 3) "))
    hole2 = int(input("How many putts for hole 2? (par is 3) "))
    hole3 = int(input("How many putts for hole 3? (par is 3) "))
    hole4 = int(input("How many putts for hole 4? (par is 3) "))
    hole5 = int(input("How many putts for hole 5? (par is 3) "))
    hole6 = int(input("How many putts for hole 6? (par is 3) "))
    total = [hole1, hole2, hole3, hole4, hole5, hole6]
    score = 0
    score = sum(total, start=score)
    game_score = score - 18
    if game_score > 0:
        print(f"Nice try, {user_name}... Your total score was + {game_score}")
    elif game_score < 0:
        print(f"Great Job, {user_name}! Your total score was {game_score}")
    else:
        print(f"Good game, {user_name}. Your total score was: 0")
