from music import Note
from player import play

from music import notes, Semitones, Reference
from exercise import build_ascending_scale_exercise


intervals = [Semitones(i) for i in range(2, 9)]
exs = build_ascending_scale_exercise(intervals=intervals)

for (a, b, c) in exs:
    print('-' * 50)
    print(a, b, c)
    play(a)
    play(b)
