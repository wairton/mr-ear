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



i = [
	('uni', 0), ('second', 2), ('third', 4), ('fourth', 5),
    ('fifth', 7), ('sixth', 9), ('seventh', 11), ('octave', 12)
]

A = 49

rnd.shuffle(i)
for ii in i:
    ans, delta = ii
    build_midi([A, A + delta])
    pygame.mixer.music.load("sample.mid")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(5)
    answer = raw_input("which interval? ").strip()
    print(ans, answer)
