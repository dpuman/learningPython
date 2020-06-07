from abc import ABC, abstractclassmethod


# class UIControll:
#     @abstractclassmethod
#     def draw(self):
#         pass


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
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

# Nb:But we need a Base Class for Common interface
