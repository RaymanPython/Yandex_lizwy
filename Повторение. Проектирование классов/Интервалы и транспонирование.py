N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.index = PITCHES.index(note)
        self.is_long = is_long
        self.ss = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и', 'фа': 'фа-а',
                   'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __str__(self):
        if self.is_long:
            return self.ss[self.note]
        else:
            return self.note

    def __eq__(self, o):
        if self.index == o.index:
            return True
        return False

    def __ne__(self, o):
        if self.index != o.index:
            return True
        return False

    def __lt__(self, o):
        if self.index < o.index:
            return True
        return False

    def __le__(self, o):
        if self.index <= o.index:
            return True
        return False

    def __gt__(self, o):
        if self.index > o.index:
            return True
        return False

    def __ge__(self, o):
        if self.index >= o.index:
            return True
        return False

    def __lshift__(self, o):
        return Note(PITCHES[(self.index - o) % N], self.is_long)

    def __rshift__(self, o):
        return Note(PITCHES[(self.index + o) % N], self.is_long)

    def get_interval(self, o):
        return INTERVALS[abs(self.index - o.index)]
