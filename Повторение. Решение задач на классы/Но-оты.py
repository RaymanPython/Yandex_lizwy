class Note():
    def __init__(self, s, f=False):
        self.s = s
        self.f = f
        if f:
            self.a = {"до": "до-о", "ре": "ре-э", "ми": "ми-и", "фа": "фа-а",
                      "соль": "со-оль", "ля": "ля-а", "си": "си-и"}

    def __str__(self):
        if self.f:
            return self.a[self.s]
        else:
            return self.s
