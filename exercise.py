import random
from music import Note, notes, Reference, Semitones


def get_random_note(lower=None, higher=None):
    lower = lower or Note('A', 0)
    higher = higher or Note('C', 8)
    n = random.randint(0, higher - lower)
    Player().perform([lower + Semitones(n)])


def build_ascending_scale_exercise(min_root=notes.C2, max_root=notes.B5, intervals=[Semitones(1)]):
   min_reference = Reference.note_to_reference(min_root)
   max_reference = Reference.note_to_reference(max_root)
   exercises = []
   for i in range(10):
       root_note = Reference.reference_to_note(random.randint(min_reference, max_reference))
       interval = random.choice(intervals)
       other_note = root_note + interval
       exercises.append((root_note, other_note, interval))
   return exercises


class Exercise:
    pass


class HarmonicExercise(Exercise):
    pass


class MelodicExercise(Exercise):
    pass


def get_random_note(min_note=notes.C1, max_note=notes.B5):
   min_reference = Reference.note_to_reference(min_note)
   max_reference = Reference.note_to_reference(max_note)
   return Reference.reference_to_note(random.randint(min_reference, max_reference))


class IntervalIdentificationMelodicExercise(MelodicExercise):
    def __init__(self, **config):
        self.config = {
            'min_root': config.get('min_root', notes.C2),
            'max_root': config.get('max_root', notes.B5),
            'intervals': config.get('intervals', [Semitones(1)]),
            'repetition': config.get('repetition', 10)
        }

    def generate_exercises(self):
        exercises = []
        for i in range(self.config['repetition']):
            root_note = get_random_note(self.config['min_root'], self.config['max_root'])
            interval = random.choice(self.config['intervals'])
            other_note = root_note + interval
            exercises.append((root_note, other_note, interval))
        return exercises


class MelodicExerciseStep:
    def __init__(self):
        pass
