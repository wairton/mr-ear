import pygame
import random as rnd
from midiutil import MIDIFile

pygame.init()

def build_midi(sequence):
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    = 80   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(sequence):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

    with open("sample.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)



class NoteFamily(object):
	def __init__(self, name, zero, alt_name=0):
		self.zero = zero

	def __getitem__(self, n):
		if not 0 <= n <= 8:
			raise IndexError
		return self.zero + 12 * n


class MidiTranslator(object):
    @classmethod
    def note_to_code(cls, note):
        # A0 = 21
        f = ord(note.base[0].lower()) - ord('a')
        if len(note.base) > 1:
            if note.base[1] == '#':
                f += 1
            else: # TODO error prone condition?
                f -= 1
            f = (f + 12) % 12
        return f + 12 * note.octave + 21

    @classmethod
    def code_to_note(cls, code):
        code -= 21
        s = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
        return Note(s[code % 12], code // 12)


class Note(object):
    def __init__(self, base, octave):
        self.base = base
        self.octave = octave

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not self._is_base_valid(value):
            raise Exception('{} is not a valid note'.format(value))
        self._base = value

    @property
    def octave(self):
        return self._octave

    @octave.setter
    def octave(self, value):
        if 0 > value or 8 < value:
            raise Exception('{} is not a valid octave'.format(value))
        self._octave = value

    def _is_base_valid(self, base):
        return base.lower()[0] in 'abcdefg' and (len(base) == 1 or base[1] in 'b#')

    def is_valid_octave(self, octave):
        return None

    def __str__(self):
        return "Note: {}{}".format(self.base.upper(), self.octave)


    # TODO for intervals, what about other notes?
    def __add__(self, interval):
        print MidiTranslator.code_to_note(MidiTranslator.note_to_code(self) + interval.semitones)


class Interval(object):
    # TODO: this tables only works for one octave
    _semi_to_symbol = {n: v for n, v in enumerate(['t', '2m', '2', '3m', '3', '4', '5m', '5', '6m', '6', '7m', '7'])}
    _symbol_to_semi = {v: n for n, v in enumerate(['t', '2m', '2', '3m', '3', '4', '5m', '5', '6m', '6', '7m', '7'])}

    def __init__(self, symbol, ascending=True):
        self.ascending = ascending
        self.symbol = symbol
        self._semitones = Interval._symbol_to_semi[symbol]

    def __str__(self):
        # TODO this only works for ascending...
        return "Interval: {} Ascending ({}) semitone(s)".format(self.symbol, self.semitones)

    @property
    def semitones(self):
        if not self.ascending:
            return - self._semitones
        return self._semitones


i = [
	('uni', 0), ('second', 2), ('third', 4), ('fourth', 5),
    ('fifth', 7), ('sixth', 9), ('seventh', 11), ('octave', 12)
]


# A = 49
A = Note('A', 4)
# print Interval('7m')
# print Interval('7m', False)
# Note('Z', 1)

A +  Interval('3m')

import sys
sys.exit(1)
rnd.shuffle(i)
for ii in []:
    ans, delta = ii
    build_midi([A, A + delta])
    pygame.mixer.music.load("sample.mid")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(5)
    answer = raw_input("which interval? ").strip()
    print(ans, answer)
