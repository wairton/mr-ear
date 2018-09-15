SHARP_NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
ATTR_SHARP_NOTES = ['A', 'AS', 'B', 'C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS']
FLAT_NOTES = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

NOTES_TABLE = {b:a for a, b in enumerate(SHARP_NOTES)}
NOTES_TABLE.update({b:a for a,b in enumerate(ATTR_SHARP_NOTES)})


i = [
	('uni', 0), ('second', 2), ('third', 4), ('fourth', 5),
    ('fifth', 7), ('sixth', 9), ('seventh', 11), ('octave', 12)
]


class Reference:
    @classmethod
    def note_to_reference(cls, note):
        # A0 = 21
        val = NOTES_TABLE[note.base.upper()]
        return val + 12 * note.octave

    @classmethod
    def reference_to_note(cls, code):
        n = Note(SHARP_NOTES[code % 12], code // 12)
        return n


class NoteFamily:
	def __init__(self, name, zero, alt_name=0):
		self.zero = zero

	def __getitem__(self, n):
		if not 0 <= n <= 8:
			raise IndexError
		return self.zero + 12 * n


class Note:
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

    def __lt__(self, other):
        return Reference.reference_to_code(self) < Reference.reference_to_code(other)

    def __eq__(self, other):
        return Reference.reference_to_code(self) == Reference.reference_to_code(other)

    # TODO: should return 'semitone' or 'interval' objects
    def __sub__(self, other):
        return Reference.reference_to_code(self) - Reference.reference_to_code(other)

    @property
    def octave(self):
        return self._octave

    @octave.setter
    def octave(self, value):
        if 0 > value or 8 < value:
            raise Exception('{} is not a valid octave'.format(value))
        self._octave = value

    def _is_base_valid(self, base):
        return base.lower()[0] in 'abcdefg' and (len(base) == 1 or base[1] in 'b#S')

    def is_valid_octave(self, octave):
        return None

    def __str__(self):
        return "Note: {}{}".format(self.base.upper(), self.octave)

    # TODO for intervals, what about other notes?
    # what about using operators like | to create chords?
    def __add__(self, interval):
        if isinstance(interval, Semitones):
            distance = interval.n
        else:
            distance = interval.semitones
        return Reference.reference_to_note(Reference.note_to_reference(self) + distance)


class Interval:
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


# TODO this name is confusing...
class Semitones:
    def __init__(self, n=1):
        self.n = n

    def __str__(self):
        return "Semitone({})".format(self.n)


class _Notes:
    def __init__(self):
        expr = ((i, j) for i in ATTR_SHARP_NOTES for j in range(1, 8))
        for (i, j) in expr:
            setattr(self, "{}{}".format(i, j), Note(i, j))

    def __iter__(self):
        expr = ((i, j) for i in ATTR_SHARP_NOTES for j in range(1, 8))
        for (i, j) in expr:
            yield getattr(self, "{}{}".format(i, j))

notes = _Notes()
