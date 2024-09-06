# Lynx

Lynx is an interactive, NLP-based Python chatbot and virtual assistant designed to provide users with a conversational experience. Lynx can perform calculations, share jokes, provide fun facts, calculate areas and perimeters of shapes, play games, track moods, and more—all through natural language interactions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Natural Language Processing**: Interact with Lynx using natural language prompts.
- **Calculations**: Perform basic arithmetic operations and complex expressions.
- **Shape Calculations**:
  - Calculate the area of various shapes (rectangle, square, triangle, circle, parallelogram).
  - Calculate the perimeter of shapes.
- **Chatbot Interactions**:
  - Tell jokes and share fun facts.
  - Provide motivational quotes.
  - Track user mood and respond accordingly.
- **Games**: Play a number-guessing game.
- **Personalized Experience**: Lynx remembers your name and personalizes responses.
- **History Tracking**: Keeps a history of calculations and interactions.
- **Help Guide**: Offers a help section to understand available commands.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/lynx-chatbot.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd lynx-chatbot
   ```

3. **Ensure Python is Installed**

   Lynx requires Python 3.x to run. You can check your Python version with:

   ```bash
   python --version
   ```

4. **Install Required Dependencies**

   Lynx uses only standard Python libraries, so no additional packages are required. However, ensure you have the following modules (which are typically included with Python):

   - `math`
   - `pickle`
   - `random`
   - `datetime`
   - `os`

## Usage

Run the `lynx.py` script to start the chatbot:

```bash
python lynx.py
```

Upon starting, Lynx will greet you and ask for your name to personalize the experience. You can then interact with Lynx using natural language prompts.

## Examples

Here are some ways you can interact with Lynx:

- **Perform Calculations**

  ```plaintext
  You: Can you calculate 5 * (2 + 3)?
  Lynx: The result of 5 * (2 + 3) is 25
  ```

- **Ask for a Joke**

  ```plaintext
  You: Tell me a joke.
  Lynx: Why don’t skeletons fight each other? They don’t have the guts.
  ```

- **Get a Fun Fact**

  ```plaintext
  You: Share a fun fact.
  Lynx: Fun fact: Bananas are berries, but strawberries aren’t!
  ```

- **Calculate Area**

  ```plaintext
  You: What's the area of a circle with radius 5?
  Lynx: The area of circle is 78.53981633974483
  ```

- **Play a Game**

  ```plaintext
  You: Let's play a game.
  Lynx: Let's play a game! I'm thinking of a number between 1 and 20.
  ```

- **Track Mood**

  ```plaintext
  You: I'm feeling stressed.
  Lynx: Take a deep breath. You've got this, and I'm here to help if you need a break.
  ```

- **Ask for Help**

  ```plaintext
  You: Help me understand what you can do.
  Lynx: [Displays help guide with available features]
  ```

## Dependencies

Lynx relies on Python's standard library modules:

- `math`
- `pickle`
- `random`
- `datetime`
- `os`

Ensure you have Python 3.x installed on your system.

## Contributing

Contributions are welcome! If you'd like to improve Lynx or add new features:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

---

Enjoy interacting with Lynx! If you encounter any issues or have suggestions, feel free to open an issue on GitHub.
