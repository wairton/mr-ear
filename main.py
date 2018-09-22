from music import Note
from player import play

from music import notes, Semitones, Reference
from exercise import IntervalIdentificationMelodicExercise


intervals = [Semitones(i) for i in range(2, 9)]
exercise = IntervalIdentificationMelodicExercise(intervals=intervals, repetition=5)


for (a, b, c) in exercise.generate_exercises():
    print('-' * 50)
    print(a, b, c)
    play(a)
    play(b)
