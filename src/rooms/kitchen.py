import turtle as t
from room import RoomObject

screen = t.Screen()
screen.bgpic('../images/kitchen.gif')

# --- creates objects ---
microwave = RoomObject(color='red', shape='circle', xcor=-50, ycor=20)
oven = RoomObject(color='red', shape='circle', xcor=-10, ycor=-100)
cabinet = RoomObject(color='red', shape='circle', xcor=-45, ycor=125)


screen.mainloop()