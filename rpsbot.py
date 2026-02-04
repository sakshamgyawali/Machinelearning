import random

def player(prev_play, opponent_history=[]):

    # Accept only valid moves
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    # If opponent repeats same move 3 times, counter it
    if len(opponent_history) >= 3:
        if opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
            return {"R": "P", "P": "S", "S": "R"}[opponent_history[-1]]

    # Count opponent moves
    counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    # Find most common move
    most_common = max(counts, key=counts.get)

    # Play the counter move
    return {"R": "P", "P": "S", "S": "R"}[most_common]
