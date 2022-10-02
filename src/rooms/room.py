import turtle as t


class RoomObject:
    def __init__(self, color, shape, xcor, ycor):
        self.object = t.Turtle()
        self.object.hideturtle()
        self.object.shape(shape)
        self.object.penup()
        self.object.goto(xcor, ycor)
        self.object.color(color)
        self.object.showturtle()

    def onClick(self):
        pass
