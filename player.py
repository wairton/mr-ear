import pygame
import io
from midiutil import MIDIFile
from midi import MidiTranslator


def note_wrapper(note):
    track = 0
    channel = 0
    time = 0    # In beats
    duration = 1    # In beats
    tempo = 80   # In BPM
    volume = 100  # 0-127, as per the MIDI standard
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)
    MyMIDI.addNote(track, channel, MidiTranslator.note_to_code(note), 0, duration, volume)
    mfile = io.BytesIO()
    MyMIDI.writeFile(mfile)
    return mfile




def build_midi(sequence):

    for i, pitch in enumerate(sequence):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

    with open("sample.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)


pygame.init()

def play(note):
    midi_note = note_wrapper(note)
    midi_note.seek(0)
    pygame.mixer.music.load(midi_note)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(5)
