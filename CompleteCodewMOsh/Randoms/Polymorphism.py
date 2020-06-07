from abc import ABC, abstractclassmethod


class UIControll:
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControll):
    def draw(self):
        print("TextBox")


class DropDownList(UIControll):
    def draw(self):
        print("DropDownList")


def draw(controlls):
    for controll in controlls:
        controll.draw()


# print(isinstance(ddl, UIControll))
# draw(ddl)
# draw(textbox)
textbox = TextBox()
ddl = DropDownList()
draw([ddl, textbox])
