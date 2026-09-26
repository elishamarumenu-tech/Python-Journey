import turtle
import random


def setup_race_track():
    """Sets up the screen, track title, and finish line."""
    screen = turtle.Screen()
    screen.title("Python Turtle Race!")
    screen.setup(width=800, height=500)
    screen.bgcolor("#2b2b2b")

    # Draw Finish Line
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.color("white")
    drawer.penup()
    drawer.goto(250, 180)
    drawer.pendown()
    drawer.right(90)
    drawer.pensize(5)
    drawer.forward(360)
    
    # Label Finish Line
    drawer.penup()
    drawer.goto(250, 190)
    drawer.write("FINISH", align="center", font=("Arial", 14, "bold"))
    drawer.hideturtle()
    
    return screen


def main():
    screen = setup_race_track()

    # Available colors and turtle setup values
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-120, -70, -20, 30, 80, 130]
    all_turtles = []

    # Get user bet via popup dialog
    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race?\nChoose a color ({', '.join(colors)}):"
    )

    if user_bet:
        user_bet = user_bet.lower().strip()

    # Create 6 turtles and place them at starting positions
    for index in range(6):
        racer = turtle.Turtle(shape="turtle")
        racer.color(colors[index])
        racer.penup()
        racer.goto(x=-350, y=y_positions[index])
        all_turtles.append(racer)

    is_race_on = False
    if user_bet in colors:
        is_race_on = True
    else:
        print("Invalid color chosen or bet canceled. Starting demo race...")
        is_race_on = True

    # Main Race Loop
    while is_race_on:
        for racer in all_turtles:
            # Check if any turtle crossed the finish line (x >= 230)
            if racer.xcor() > 230:
                is_race_on = False
                winning_color = racer.pencolor()

                # Display result on screen
                result_display = turtle.Turtle()
                result_display.hideturtle()
                result_display.penup()
                result_display.color("white")

                if winning_color == user_bet:
                    message = f"You won! The {winning_color} turtle is the winner!"
                else:
                    message = f"You lost! The {winning_color} turtle won the race!"

                result_display.write(message, align="center", font=("Arial", 18, "bold"))
                break

            # Move turtle forward by a random step distance between 1 and 10
            rand_distance = random.randint(1, 10)
            racer.forward(rand_distance)

    screen.exitonclick()


if __name__ == "__main__":
    main()