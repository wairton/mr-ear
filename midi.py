class MidiTranslator:
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
