from turtle import Turtle, Screen
import random

s = Screen()
is_race_on = False
s.setup(width=500,height=400)
user_best = s.textinput(title="Mack you bet", prompt="choose your turtle color: ")
color = ["red","green", "orange", "blue", "black"]
all_t = []
x=-230
y=-100
for n in range(5):
	n_t = Turtle(shape="turtle")
	n_t.color(color[n])
	n_t.penup()
	n_t.goto(x,y)
	y += 50
	all_t.append(n_t)

if(user_best):
	is_race_on = True

while is_race_on:
	for t in all_t:
		if t.xcor() > 230:
			is_race_on = False
			win_color = t.pencolor()
			if user_best == win_color:
				print(f"you won!,the winner is {win_color} turtle")
			else:
				print(f"you loose!,the winner is {win_color} turtle")
		rand_move = random.randint(1,10)
		t.forward(rand_move)




s.exitonclick()