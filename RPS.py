# RPS.py

import random

def player(prev_play, opponent_history=[], my_history=[]):
    # Track opponent's history
    if prev_play:
        opponent_history.append(prev_play)

    # If no history yet, start with random
    if not opponent_history:
        guess = random.choice(["R", "P", "S"])
    else:
        # Count frequencies of opponent moves
        counts = {"R": opponent_history.count("R"),
                  "P": opponent_history.count("P"),
                  "S": opponent_history.count("S")}

        # Assume opponent will play their most frequent move
        prediction = max(counts, key=counts.get)

        # Counter strategy: play the winning move
        beats = {"R": "P", "P": "S", "S": "R"}
        guess = beats[prediction]

        # --- Simple pattern detection ---
        if len(opponent_history) >= 3:
            last3 = "".join(opponent_history[-3:])
            patterns = {}
            for i in range(len(opponent_history)-3):
                seq = "".join(opponent_history[i:i+3])
                if seq == last3 and i+3 < len(opponent_history):
                    nxt = opponent_history[i+3]
                    patterns[nxt] = patterns.get(nxt, 0) + 1
            if patterns:
                prediction = max(patterns, key=patterns.get)
                guess = beats[prediction]

    # Save my move
    if len(my_history) < len(opponent_history):
        my_history.append(guess)
    else:
        if my_history:
            my_history[-1] = guess
        else:
            my_history.append(guess)

    return guess
