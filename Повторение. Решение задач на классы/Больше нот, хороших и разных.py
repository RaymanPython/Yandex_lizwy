PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, qw=PITCHES[0], is_long=False):
        self.note = qw
        self.long = is_long
        self.up = False
        self.oc = ''

    def __str__(self):
        if self.long:
            if self.note[0] == 'д':
                if self.up:
                    d = 'до-о'.upper()
                else:
                    d = 'до-о'
            if self.note[0] == 'р':
                if self.up:
                    d = 'ре-э'.upper()
                else:
                    d = 'ре-э'
            if self.note[0] == 'м':
                if self.up:
                    d = 'ми-и'.upper()
                else:
                    d = 'ми-и'
            if self.note[0] == 'ф':
                if self.up:
                    d = 'фа-а'.upper()
                else:
                    d = 'фа-а'
            if self.note[0:2] == 'со':
                if self.up:
                    d = 'со-оль'.upper()
                else:
                    d = 'со-оль'
            if self.note[0] == 'л':
                if self.up:
                    d = 'ля-а'.upper()
                else:
                    d = 'ля-а'
            if self.note[0:2] == 'си':
                if self.up:
                    d = 'си-и'.upper()
                else:
                    d = 'си-и'
        else:
            if self.up:
                d = str(self.note).upper()
            else:
                d = self.note
        if self.oc != '':
            d += ' (' + self.oc + ')'
        return d


class DefaultNote(Note):
    def __init__(self, qw=PITCHES[0], is_long=False):
        self.note = qw
        self.long = is_long
        self.up = False
        self.oc = ''


class LoudNote(Note):
    def __init__(self, qw=PITCHES[0], is_long=False):
        self.note = qw
        self.long = is_long
        self.up = True
        self.oc = ''


class NoteWithOctave(Note):
    def __init__(self, qw=PITCHES[0], qwer="первая октава", is_long=False):
        self.note = qw
        self.long = is_long
        self.up = False
        self.oc = qwer
