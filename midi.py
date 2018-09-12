from music import Reference


class MidiTranslator:
    @classmethod
    def note_to_code(cls, note):
        return  Reference.note_to_reference(note) + 21

    @classmethod
    def code_to_note(cls, code):
        code -= 21
        s = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
        # return Note(s[code % 12], code // 12)
