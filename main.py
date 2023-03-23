import turtle
import pandas

data = pandas.read_csv("states.csv")

screen = turtle.Screen()
screen.title("Indian states")
image = "India-Map.gif"
screen.addshape(image)
turtle.shape(image)
is_on = True
guess_count = 0
state_list = list(data["States"])
guess_states = []

while len(guess_states) < 27:
    answer_state = screen.textinput(title=f"{guess_count}/27 States correct", prompt="What is another state name")
    if answer_state == "exit":
        learn_state = [state for state in state_list if state not in guess_states]  # List comprehension
        data_csv = pandas.DataFrame(learn_state)
        data_csv.to_csv("learn state.csv")
        break
    if answer_state in state_list:
        guess_states.append(answer_state)
        guess_count += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("red")
        state_data = data[data.States == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.goto(data._get_value(state_list.index(f"{answer_state}"), "x"),
        #        data._get_value(state_list.index(f"{answer_state}"), "y"))
        t.write(f"{answer_state}", font=("Arial", 8, "normal"))

# for i in state_list:
#     if i in guess_states:
#         pass
#     else:
#         learn_state.append(i)
