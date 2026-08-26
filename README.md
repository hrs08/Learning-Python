🐍 Learning Python
██████╗  ██╗   ██╗  ████████╗  ██╗  ██╗   ██████╗  ███╗   ██╗
██╔══██╗ ╚██╗ ██╔╝  ╚══██╔══╝  ██║  ██║  ██╔═══██╗ ████╗  ██║
██████╔╝  ╚████╔╝      ██║     ███████║  ██║   ██║ ██╔██╗ ██║
██╔═══╝    ╚██╔╝       ██║     ██╔══██║  ██║   ██║ ██║╚██╗██║
██║         ██║        ██║     ██║  ██║  ╚██████╔╝ ██║ ╚████║
╚═╝         ╚═╝        ╚═╝     ╚═╝  ╚═╝   ╚═════╝  ╚═╝  ╚═══╝

                    L E A R N I N G   P Y T H O N

📚 Learning Python

Welcome to my Python learning and revision journey.

This repository is my personal coding journal where I practice Python, revisit concepts I've already learned, learn new topics, and build projects to make sure the knowledge actually sticks.

Unlike my C learning journey, this repository isn't focused on simply completing a course from start to finish.

Instead, I'm using Python to revise my fundamentals, learn new concepts, experiment with different features, and turn what I learn into actual projects.

🧠 Learn → Revise → Practice → Build → Repeat

📊 Repository Stats
🐍 Python learning and revision
📚 Fundamentals continuously revisited
🧠 New concepts learned alongside revision
🛠️ Multiple practice programs and mini projects
🏗️ Object-Oriented Programming
🎀 Decorators, properties, and dunder methods
⏰ Date and time programming
🚨 Exception and file handling
🎵 Larger projects in progress
🚀 Goal: Build increasingly complex Python applications
🎯 Why This Repo?

I'm keeping this repository to:

🧠 Keep Python concepts fresh
💻 Practice by actually writing code
📈 Track my progress over time
🔄 Revisit concepts instead of forgetting them
🛠️ Turn concepts into working programs
🧩 Improve my problem-solving skills
🧹 Gradually write cleaner code
🚀 Build projects instead of only following tutorials

The goal isn't simply to remember Python syntax.

The goal is to reach the point where I can think about a problem, choose the right tools, and build something with Python.

📖 Learning Approach

My approach to Python is simple:

        LEARN
          ↓
        REVISE
          ↓
       PRACTICE
          ↓
        BUILD
          ↓
     BREAK THINGS
          ↓
        FIX THEM
          ↓
      UNDERSTAND
          ↓
        REPEAT


Some topics in this repository are things I'm learning for the first time.

Others are concepts I've already encountered and am revisiting so they become easier to use naturally.

📂 Repository Structure

Each part of the repository contains different kinds of Python work:

📚 Revision — Revisiting concepts I've already learned
🧪 Experiments — Small programs for understanding specific features
📝 Practice — Exercises and concept-based programs
🛠️ Mini Projects — Small applications combining multiple concepts
🚀 Projects — Larger applications that require several concepts together

As I improve, I may return to older programs and refactor them to compare my earlier code with newer implementations.

📚 Topics Learned & Revised
🟢 Python Fundamentals
Basic Python syntax
print()
Comments
Variables
Strings
Integers
Floats
Booleans
type()
F-strings
User input with input()
Mathematical operations
Expressions
Type casting
str()
int()
float()
bool()
Truthy and falsy values
🔀 Control Flow
if
elif
else
Logical operators
Boolean conditions
while loops
for loops
Nested control flow
break
continue
Iterating through strings
Iterating through collections
🧮 Problem Solving

Practiced turning simple problems into working Python programs.

Examples include:

📐 Rectangle Area Calculator
🛒 Shopping Cart
📝 Mad Libs
🧮 Calculator
🔢 Mathematical exercises
⌨️ User-input-based programs

These programs may be simple, but they help reinforce the fundamentals before moving into more complicated projects.

📦 Lists & Collections

Practiced working with lists and collections through different programs.

Topics include:

Creating lists
Indexing
Iterating through lists
.copy()
.index()
Lists containing objects
Using lists with loops
Modifying collections
Passing collections around programs
📦 Modules & Imports

Learning how Python's modules can provide additional functionality and help organize larger programs.

Modules practiced
random
string
datetime
time

I've also practiced separating classes and functionality into different files instead of keeping everything inside one large Python file.

🎲 Random Module

Practiced:

Random number generation
random.shuffle()
Creating randomized keys
Copying lists
Combining randomness with strings and lists

These concepts were used in my basic encryption/decryption project.

🔐 Basic Encryption Program

Built a basic character-substitution encryption and decryption program.

The program:

Creates a collection of characters
Copies the collection
Randomly shuffles the copy
Uses character indexes to create a substitution key
Encrypts the user's message
Uses the same key to decrypt the message
Concepts practiced
random
string
Lists
.copy()
.index()
random.shuffle()
Loops
Strings
User input
String construction

⚠️ This is a learning project and not a secure encryption system.

🏗️ Object-Oriented Programming

A major part of my Python learning has been Object-Oriented Programming (OOP).

Classes & Objects

Practiced:

Creating classes
Creating objects
__init__()
Instance attributes
Instance methods
Class variables
self
Organizing classes into separate files

Example:

class Car:
    wheel = 4

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

🧬 Inheritance

Practiced:

Parent classes
Child classes
Inheriting attributes
Inheriting methods
Multilevel inheritance
Multiple inheritance
Reusing functionality
Method inheritance

Examples included:

Animal
├── Dog
├── Cat
├── Prey
│   └── Rabbit
└── Predator
    └── Hawk


I also experimented with multiple inheritance using a class that inherits from both Prey and Predator.

🔗 super()

Learned how super() can be used to access functionality from a parent class.

This is particularly useful when a child class needs to reuse or extend the behavior of its parent class.

🎭 Polymorphism

Practiced polymorphism, where different objects can respond to the same method call in their own way.

For example:

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()


Both objects can use the same speak() method while providing different behavior.

🦆 Duck Typing

Explored Python's duck typing philosophy:

If it looks like a duck and quacks like a duck, treat it like a duck.

Rather than always focusing on an object's exact type, Python can focus on whether an object provides the behavior that is required.

⚙️ Instance, Static & Class Methods

Practiced the differences between several types of methods.

Instance Methods

Use self to work with a specific object.

Static Methods

Use @staticmethod when the method doesn't need access to the instance or class.

Class Methods

Use @classmethod and cls to work with the class itself.

Topics practiced:

self
cls
Instance methods
@staticmethod
@classmethod
Class variables
Object-specific data
Class-level data
🪄 Magic / Dunder Methods

Explored Python's special methods and how they can customize object behavior.

Practiced:

Method	Purpose
__init__()	Initialize objects
__str__()	Customize string representation
__eq__()	Compare objects
__lt__()	Less-than comparison
__add__()	Customize +
__contains__()	Customize in
__getitem__()	Customize [] access

For example:

def __str__(self):
    return f"{self.title} by {self.author}"


This allows an object to control how it is represented as a string.

🏷️ Properties

Learned how @property can be used to control access to object attributes.

Practiced:

@property
Getters
Setters
Deleters
Attribute validation
Controlled attribute access

I practiced this using a Rectangle class where width and height could be validated when changed.

🎀 Decorators

Learned that decorators can extend the behavior of functions without directly modifying the original function.

Basic example:

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("** You added sprinkles 🍦 **")
        func(*args, **kwargs)

    return wrapper


Then applying it with:

@add_sprinkles
def get_icecream():
    print("Here is your ice cream!")


This helped me understand the basic idea behind function wrapping and decorators.

🚨 Exception Handling

Started learning about exception handling and how Python programs can deal with unexpected situations.

The goal is to make programs more robust instead of allowing every unexpected situation to immediately terminate the program.

This is an area I want to continue strengthening through practical projects.

📂 File Handling

Practiced the fundamentals of working with files.

Topics include:

Opening files
Reading files
Writing files
Working with file data
Using file handling inside programs

I want to use file handling more extensively in future projects.

⏰ Date & Time

Practiced working with Python's date and time functionality.

Topics include:

datetime
time
datetime.datetime.now()
.strftime()
Time formatting
time.sleep()

These concepts were used in my Python Alarm Clock project.

⏰ Python Alarm Clock

Built a simple alarm clock using Python's date and time functionality.

Features
Takes an alarm time from the user
Gets the current system time
Continuously checks the current time
Compares it with the alarm time
Triggers when the specified time is reached
Waits between checks using time.sleep()
Concepts Combined
Functions
User input
datetime
time
while loops
Conditions
String formatting
if __name__ == "__main__"
🛠️ Projects & Practice Programs
Project	Main Concepts
📝 Mad Libs	Variables, input, strings
📐 Rectangle Area Calculator	Input, floats, arithmetic
🛒 Shopping Cart	Variables, input, calculations
🧮 Calculator	Operators, input, control flow
🔐 Basic Encryption Program	Lists, strings, loops, modules
🚗 Car OOP Program	Classes, objects, methods
🐶 Animal Inheritance	OOP, inheritance, polymorphism
📚 Book Class	Dunder methods
📐 Rectangle Class	Properties, setters, getters
⏰ Alarm Clock	datetime, time, loops
🎵 TUI Music Player	Larger ongoing project
🧠 Current Understanding

At this point, I have a working understanding of:

🟢 Python fundamentals
🔤 Strings and basic data types
🔄 Type casting
⌨️ User input and output
🔀 Conditions
🔁 Loops
🔧 Functions
📦 Lists and collections
📚 Modules and imports
🎲 Randomization
📂 File handling
🚨 Exception handling
⏰ Date and time
🏗️ Classes and objects
🧬 Inheritance
🔗 Multiple and multilevel inheritance
🎭 Polymorphism
🦆 Duck typing
⚙️ Static and class methods
🏷️ Properties
🎀 Decorators
🪄 Dunder methods

I'm also learning how to combine these concepts rather than treating every topic as a separate piece of syntax.

🔄 Revision Strategy

Since I've already encountered many Python fundamentals, revision is an important part of this repository.

Instead of simply watching tutorials repeatedly, I want to:

Rebuild concepts from memory
Write small programs
Find what I've forgotten
Revisit the concept
Apply it in a project
Refactor the code later

The goal is to move from:

"I recognize this."

to:

"I can use this."

And eventually:

"I can build something with this."

🚀 What's Next?

The focus is gradually shifting from learning individual concepts toward building larger programs.

My next goals are:

🛠️ Build larger Python projects
🎵 Continue developing the TUI music player
🧩 Combine multiple Python concepts in single projects
📚 Strengthen my knowledge of Python's standard library
🧠 Improve problem-solving skills
🧹 Refactor older programs
🧪 Experiment with unfamiliar Python features
⚡ Write cleaner and more Pythonic code
🏗️ Learn better project structure
📈 Move from small scripts toward substantial applications
📌 My Rules
✔️ Don't just watch tutorials
✔️ Write the code myself
✔️ Revise concepts I haven't used recently
✔️ Build projects
✔️ Learn from mistakes
✔️ Understand why, not just how
✔️ Don't be afraid to rewrite old code
✔️ Experiment with things I don't understand
✔️ Improve a little with every project
⚠️ Note

This repository is a record of my Python learning and revision process.

Not every program here is intended to be production-quality code.

Some programs are intentionally simple because their purpose is to practice a specific concept. Others may contain mistakes, awkward implementations, or approaches that I later discover can be improved.

That's part of the journey.

Older code represents what I understood at that point.

Newer code should gradually show how my understanding, coding style, and problem-solving ability improve over time.

🐍 The Goal

I'm not trying to simply "finish learning Python."

There isn't really a finish line.

The goal is to keep learning, keep revising, keep building, and eventually reach the point where Python becomes a tool I can use to turn an idea into something real.

Learn the syntax. Understand the concepts. Build the thing.
