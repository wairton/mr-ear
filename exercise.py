import random


def get_random_note(lower=None, higher=None):
    lower = lower or Note('A', 0)
    higher = higher or Note('C', 8)
    n = random.randint(0, higher - lower)
    Player().perform([lower + Semitones(n)])
