class a:
    res = []

    def ap(self, s):
        self.res.append(s)

    def result(self):
        return self.res


def parrot(s):
    if s in a.res:
        print(s)
    else:
        a.ap(a, s)


a()
