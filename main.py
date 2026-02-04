from RPS_bot import player

import random

def random_opponent(prev_play, history=[]):
    return random.choice(["R", "P", "S"])

opponent_history = []
player_history = []

for i in range(10):
    opponent_move = random_opponent("" if i==0 else opponent_history[-1])
    player_move = player("" if i==0 else opponent_history[-1], opponent_history)
    
    opponent_history.append(opponent_move)
    player_history.append(player_move)
    
    print(f"Game {i+1}: Player -> {player_move} | Opponent -> {opponent_move}")
