# high_score.py

def load_high_score(filename):
    try:
        with open(filename, 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def save_high_score(filename, score):
    with open(filename, 'w') as f:
        f.write(str(score))
