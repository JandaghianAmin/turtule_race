from turtle import Turtle, Screen
import random


turtul_color= ["red","green","blue","yellow","black","orange"]
y_pos = [-70,-40,-10,20,50,80]
y=-100
my_screen = Screen()
user_bet = my_screen.textinput(title="whih color wins?",prompt=" red, green, blue, yellow, black or orange :")
while user_bet not in turtul_color:
    user_bet = my_screen.textinput(title="whih color wins?",prompt=" red, green, blue, yellow, black or orange :")

my_screen.setup(width=500,height=400)
all_turtule = []

for i in range(0,6):
    tur = Turtle(shape="turtle")
    tur.color(turtul_color[i])
    tur.penup()
    tur.goto(-240,y_pos[i])
    all_turtule.append(tur)


is_finish = False
while not is_finish:
    for turt in all_turtule:
        turt.forward(random.randint(0,10))
        if turt.xcor() > 230:
            is_finish=True
            # print(f"Game Over! and {turt.pencolor()} turtle win the game.")
            # if user_bet == turt.pencolor():
            #     print("You Win Horaaaaa :)")
            # else:
            #     print(f"{user_bet} turtle Lose. :(")



pos ={}
for pos_turtl in all_turtule:
    pos[pos_turtl.pencolor()]=pos_turtl.xcor()

sorted_turtle = sorted(pos.items(), key=lambda x:x[1],reverse=True)
 

is_win = True
for key,value in pos.items():
    if value > pos[user_bet] :
        is_win = False


 

if is_win:
     print("You Win Horaaaaa :)")
else:
    print(f"{user_bet} turtle Lose.")   
print(".............Result Table...................")
print(sorted_turtle)     
print("............................................")
print(f"Winner is {sorted_turtle[0]}")
        





            






my_screen.exitonclick()