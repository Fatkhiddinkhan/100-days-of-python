import turtle
import pandas

# screen config
screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50:
    user_prompt = screen.textinput(title=f"{len(guessed_state)}/50 Guessed Correctly", prompt="What is the next State?").title()
    if user_prompt == "Exit":
        states_to_learn = []
        for state in data.state:
            if state not in states_to_learn:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_prompt in all_states:
        guessed_state.append(user_prompt)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_prompt]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_prompt)

# states_to_learn.csv
