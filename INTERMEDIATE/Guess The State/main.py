from turtle import Turtle, Screen, shape
import pandas as pd

screen = Screen()
screen.title("India State Game")
image = 'india.gif'
screen.addshape(image)
shape(image)

# Get Coordinates of the states
# def get_mouse_click_cor(x, y):
#     print(f"{x},{y}")
# turtle.onscreenclick(get_mouse_click_cor)

data = pd.read_csv('india.csv')
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) < len(data.states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(data.states)}", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.color("red")
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.states.item())
