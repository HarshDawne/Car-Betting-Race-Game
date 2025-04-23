from turtle import Turtle, Screen
from tkinter import messagebox
import random

# Setup screen
screen = Screen()
screen.title("Car Racing Game")
screen.setup(width=800, height=500)

# Car colors and images
car_colors = ['red', 'blue', 'green', 'orange', 'black']
image_paths = ['car1.gif', 'car2.gif', 'car3.gif', 'car4.gif', 'car5.gif']
y_positions = [-200, -100, 0, 100, 200]

# Ask user for their guess
user_choice = screen.textinput("Choose Your Car", f"Pick a car color from {car_colors}:").lower()

# Register images and create cars
cars = []
for i in range(5):
    screen.addshape(image_paths[i])
    car = Turtle()
    car.shape(image_paths[i])
    car.penup()
    car.name = car_colors[i]
    car.goto(-350, y_positions[i])
    cars.append(car)

# Start the race
race_on = True
while race_on:
    car = random.choice(cars)
    car.forward(random.randint(5, 15))

    if car.xcor() >= 380:
        race_on = False
        winner = car.name
        result = "won" if winner.lower() == user_choice else "lost"
        messagebox.showinfo("Race Result", f"🏁 Winner: {winner.upper()}!\nYou {result.upper()} the bet!")
        break

# Exit on click
screen.exitonclick()
