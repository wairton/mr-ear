import pygame
from midiutil import MIDIFile


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


pygame.init()

def player():
    ans, delta = ii
    build_midi([A, A + delta])
    pygame.mixer.music.load("sample.mid")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(5)
    answer = raw_input("which interval? ").strip()
    print(ans, answer)
