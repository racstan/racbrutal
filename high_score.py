# high_score.py

import os

def save_high_score(score):
    with open('high_score.txt', 'w') as f:
        f.write(str(int(score)))

def load_high_score():
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as f:
            return int(f.read())
    else:
        return 0
