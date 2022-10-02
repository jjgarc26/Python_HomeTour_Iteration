import turtle as t

# --- set screen up ---
screen = t.Screen()
screen.bgpic('images/house.gif')
screen.screensize(600,600)

title = t.Turtle()
title.penup()
title.hideturtle()
title.goto(0, 250)
title.color('black')
title.write(arg='Home Tour', align='center', font=('Arial',42, 'normal'))

# --- Introduction ---

intro = 'You find yourself walking down an empty stree, You' \
         'see an empty house. Something moved in a window!\n' \
         'It is dark and you are all alone, you have this urge' \
         'to check it out....but do you really want to risk it\n' \
         'for the biscut? The choice is yours'
intro_dialogue = t.Turtle()
intro_dialogue.penup()
intro_dialogue.hideturtle()
intro_dialogue.goto(0, -300)
intro_dialogue.color('black')
intro_dialogue.write(arg=intro, align='center', font=('Arial', 12, 'normal'))

# begin game

# use the screnn.update() to

screen.mainloop()