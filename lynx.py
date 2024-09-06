import math
import pickle
import random
import datetime
import os

file_name = "lynxhistory.dat"
user_name = ""

def open_file(mode):
    return open(file_name, mode)

def greet_user():
    global user_name
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    if user_name:
        print(f"{greeting}, {user_name}! How can I assist you today?")
    else:
        user_name = input(f"{greeting}! What's your name?\n")
        print(f"Nice to meet you, {user_name}! How can I assist you today?")

def mood_tracker():
    mood = input("How are you feeling today? (happy, sad, stressed, excited, tired, etc.): ").lower()
    if mood == "happy":
        print("I'm so glad to hear that! Keep up the positive vibes, you're doing great!")
    elif mood == "sad":
        print("I'm sorry you're feeling down. Remember, it's okay to have tough days. I'm here for you.")
    elif mood == "stressed":
        print("Take a deep breath. You've got this, and I'm here to help if you need a break.")
    elif mood == "excited":
        print("That's awesome! Excitement is contagious. What's making you feel so excited?")
    elif mood == "tired":
        print("Sounds like you need some rest. Make sure to take care of yourself, okay?")
    else:
        print("Thanks for sharing. I'm always here if you want to talk!")

def tell_joke():
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? It had too many problems.",
        "What did one ocean say to the other ocean? Nothing, they just waved!"
    ]
    print(random.choice(jokes))

def fun_fact():
    facts = [
        "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!",
        "Fun fact: Bananas are berries, but strawberries aren’t!",
        "Did you know? A day on Venus is longer than a year on Venus.",
        "Fun fact: There are more stars in the universe than grains of sand on all of Earth's beaches."
    ]
    print(random.choice(facts))

def random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Don't watch the clock; do what it does. Keep going.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Life is 10% what happens to us and 90% how we react to it."
    ]
    print(random.choice(quotes))

def guess_the_number():
    number = random.randint(1, 20)
    print("Let's play a game! I'm thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congrats, {user_name}! You guessed it in {attempts} attempts.")
            break

def calculations(expression):
    try:
        with open_file("ab+") as h:
            answer = eval(expression)
            print(f"The result of {expression} is {answer}")
            pickle.dump({"calculation": expression, "answer": answer}, h)
    except Exception as e:
        print(f"Error: {e}")

def calculate_area(shape, dimensions):
    with open_file("ab+") as h:
        if shape == "rectangle":
            l, b = dimensions
            area = l * b
        elif shape == "square":
            s, = dimensions
            area = s * s
        elif shape == "triangle":
            hgt, b = dimensions
            area = (b * hgt) / 2
        elif shape == "circle":
            r, = dimensions
            area = math.pi * r * r
        elif shape == 'parallelogram':
            b, hgt = dimensions
            area = b * hgt
        else:
            print("Sorry! This shape is not available.")
            return
        
        print(f"The area of {shape} is {area}")
        pickle.dump({"area": area}, h)

def perimeters(shape, dimensions):
    with open_file("ab+") as h:
        if shape == "circle":
            r, = dimensions
            perimeter = 2 * math.pi * r
        elif shape == "square":
            s, = dimensions
            perimeter = 4 * s
        elif shape == "rectangle":
            l, b = dimensions
            perimeter = 2 * (l + b)
        elif shape == "triangle":
            a, b, c = dimensions
            perimeter = a + b + c
        else:
            print("Sorry, invalid shape.")
            return

        print(f"The perimeter of {shape} is {perimeter}")
        pickle.dump({"perimeter": perimeter}, h)

def parse_input(user_input):
    user_input = user_input.lower()

    if any(keyword in user_input for keyword in ["calculate", "solve"]):
        expression = input("What expression would you like to calculate? ")
        calculations(expression)

    elif "area" in user_input:
        shape = input("Enter the shape (rectangle, square, triangle, circle, parallelogram): ").lower()
        if shape in ["rectangle", "triangle", "parallelogram"]:
            dimensions = [int(input("Enter the first dimension: ")), int(input("Enter the second dimension: "))]
        elif shape in ["circle", "square"]:
            dimensions = [int(input("Enter the dimension: "))]
        calculate_area(shape, dimensions)

    elif "perimeter" in user_input:
        shape = input("Enter the shape (circle, square, rectangle, triangle): ").lower()
        if shape == "triangle":
            dimensions = [int(input("Enter side 1: ")), int(input("Enter side 2: ")), int(input("Enter side 3: "))]
        else:
            dimensions = [int(input("Enter the dimension: "))]
        perimeters(shape, dimensions)

    elif "joke" in user_input:
        tell_joke()

    elif "fun fact" in user_input:
        fun_fact()

    elif "quote" in user_input:
        random_quote()

    elif "game" in user_input or "guess" in user_input:
        guess_the_number()

    elif "mood" in user_input:
        mood_tracker()

    elif "help" in user_input:
        help_guide()

    elif "exit" in user_input:
        print(f"Goodbye, {user_name}! Have a great day!")
        return False

    else:
        print("Sorry, I didn't quite understand. Could you try asking in a different way?")
    return True

def help_guide():
    print("""
    Welcome to Lynx! Here's what I can do:
    1. Perform basic calculations (e.g., "Calculate 5 + 3").
    2. Calculate the area of shapes (e.g., "What is the area of a rectangle?").
    3. Calculate perimeters and circumferences (e.g., "What is the perimeter of a square?").
    4. Tell a joke (e.g., "Tell me a joke").
    5. Share a fun fact (e.g., "Tell me a fun fact").
    6. Provide motivational quotes (e.g., "Give me a quote").
    7. Play a guessing game (e.g., "Let's play a game").
    8. Track your mood (e.g., "I'm feeling sad").
    9. Show your activity history.
    """)

def main():
    greet_user()
    help_guide()

    while True:
        user_input = input("\nHow can I assist you? (Type 'exit' to quit): ")
        if not parse_input(user_input):
            break

if __name__ == "__main__":
    main()
