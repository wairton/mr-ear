import random
from music import Note, notes, Reference, Semitones


def get_random_note(lower=None, higher=None):
    lower = lower or Note('A', 0)
    higher = higher or Note('C', 8)
    n = random.randint(0, higher - lower)
    Player().perform([lower + Semitones(n)])


def build_ascending_scale_exercise(min_root=notes.A2, max_root=notes.GS5, intervals=[Semitones(1)]):
   min_reference = Reference.note_to_reference(min_root)
   max_reference = Reference.note_to_reference(max_root)
   exercises = []
   for i in range(10):
       root_note = Reference.reference_to_note(random.randint(min_reference, max_reference))
       interval = random.choice(intervals)
       other_note = root_note + interval
       exercises.append((root_note, other_note, interval))
   return exercises
