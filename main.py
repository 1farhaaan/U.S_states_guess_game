import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_ans = []

while len(guessed_ans) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_ans)}/50 States", prompt="What's the another state name?").title()

    if ans_state == "Exit":
        missing_states = [data for data in all_states if data in guessed_ans]
        data_files = pandas.DataFrame(missing_states)
        data_files.to_csv("states_learn.csv")
        break

    if ans_state in all_states:
        guessed_ans.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
