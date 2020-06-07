class Text(str):
    def duplicate(self):
        return self + " " + self


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


text = Text("Dipu")

print(text.lower())
print(text.duplicate())


trac = TrackableList()
trac.append('1')
