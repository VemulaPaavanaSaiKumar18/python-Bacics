from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
Turtle(shape=image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
	if answer_state == "Exit":
		missed_states = []
		for state in states:
			if state not in guessed_states:
				missed_states.append(state)
		new_data = pandas.DataFrame(missed_states)
		new_data.to_csv("states_to_learn.csv")
		break
	if answer_state in states and answer_state not in guessed_states:
		guessed_states.append(answer_state)
		turtle = Turtle()
		turtle.penup()
		turtle.hideturtle()
		turtle.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
		turtle.write(answer_state)

screen.exitonclick()

