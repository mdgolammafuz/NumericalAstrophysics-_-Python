# Thinking like a Computer : The logic of object oriented programming

# First : Understanding Objects 

## Understanding objects in object oriented programing :

1. Objects can be designed to model real-world things in software.

2. Objects group together details.

3. Abstraction means showing only what’s relevant and useful for the person using it.

4. By hiding all the inner workings of a given object with abstraction, we are able to reduce their apparent complexity.

## Discovering Computer's inner architect - Planning out objects :

1. A plan or blueprint for an object is called a class.

2. A class defines the attributes (a description), the methods (what it does), and the access level (who can use it) for an object.

3. To create an object, you have to instantiate it. An instantiated object is called an instance of a class.

4. Objects from the same class can differ in the details if they have different values for their attributes. They still have to follow the class plan, though! 

5. Encapsulation is the bundling together of attributes, methods, and access control in order to protect an object. 

## Interact with objects - complex systems and sending messages :

1. Objects can have attributes that are objects. These objects also have their own independent blueprint (class), attributes, behaviors, and access.

2. Objects communicate with one another by sending messages.

3. Associating objects with other objects allows you to more easily adapt and make changes to your system.  


## Second : Using logic and element of programming

## Discovering how a computer solves a problem - Solving problems like a computer :

1. Computers can solve problems by performing billions of operations per second.

2. A programmer’s job is to find solutions. They do this by breaking down problems into easy-to-follow steps for a computer.

3. Programming languages allow people to communicate with computers.

4. Computers are literal and do exactly what you tell them to.

## Working with sequences - The flow of logic :

1. A logic flow is the order in which steps are completed in a program.

2. Steps are completed sequentially, not simultaneously.

3. Some steps are independent, which means they can be completed in any order.

## Working with states and logical operators :

1. Computers use logical operations to solve problems. 

2. Boolean values can be either true or false.

3. Other values are null or empty. 

4. Key logical operators are NOT, AND, OR.

## Following a sequence with conditions :

1. Use if/else statements for conditions.

2. You can compare elements using greater than, less than, and equal to.

## Iterating the instructions by working with loops :

1. While loops are used when you know the end state you want, but not the number of iterations.

2. For loops are used when you know the exact number of iterations you need.  

3. An infinite loop is a while loop that gets stuck because it doesn’t have an end condition. 


## Third : Understanding the functions

## Understanding how functions work :

1. Coding is fun but you should not duplicate time and effort: use functions for repetitive tasks.

2. Functions contain a series of instructions you can use again and again.

3. Functions have names.

4. When you need a function, you can call it by name.  

## Using functions - Black boxes, a everyday reality :

1. A black box performs something useful without needing to how it does what it does.

2. We use black box functions regularly in real life and in programming. 

## Writing clean functions - Four steps of writing functions :

Writing clean functions is critical for making sure they work well.
Good function writing takes 4 basic steps:

    1) Choose a goal and name the function accordingly

    2) Define the end result

    3) Define what the function requires as input

    4) Implement the logic


## Defining and sending messages with functions - parameters and return values :

1. Functions can receive messages through parameters.

2. Functions can send messages through return values. 


# Fourth : Learning about Data Storage  

## Where is the data ? In the Variables

1. Variables are containers where we store data. 

2. Variables are stored in specific locations in computer memory. 

3. Variables have different types. 

4. Variables have names

## Primitive datatypes - Things all computers know :

1. All computers understand the fundamental primitive data types.

2. Boolean can be only true or false.

3. String contains a series of alphanumeric characters.
Number is used in arithmetic.

4. Null is the presence of nothing.

Types define what we can put in a variable. There are different types we can use. We've actually seen one of them already: objects! These are often referred to as complex types because they're complex! 🎈

    1) Boolean: 
    As you saw previously, the Boolean data type can contain only the values true or false.  This is the only data type the computer can use to make decisions.

    2) Null: The absence of anything
    Empty is not a primitive data type, but it is a value.

    3) String: Seies of characters or symbols
    The string data type is a series of characters. By characters we mean letters or letter-like symbols used to  communicate.

    4) Number: Float or Integer
    The number data type is used for arithmetic operations.  Numbers can be positive or negative and may          contain a decimal point.


## Recognizing the array data type : 

1. An array is a container for other objects.

2. The array contains a fixed number of buckets that you specify when it is created.

3. Array buckets are accessed using zero-based counting.

4. Array processing is very fast. Array buckets can be accessed in constant time (very fast) so even if there were two-million objects inyour container, the time to fetch an objects is the same as if there were only a few objects.

## List data types - The List container :

1. List is an ordered container of objects.

2. List size is dynamic and can become bigger or smaller according to your needs. 

## Exploring the dictionary data type - The Map :

1. The map or dictionary data type stores rows of key/value pairs.

2. Rows can be added/removed for any key you wish.
Size is dynamic, and can shrink/grow in real time. 


## Summary:

    1. Identify how computers use objects in programming.

    2. Understand how computers use logic to make decisions and run programs.

    3. Explain what functions are used for in programming. 

    4. Recognize how data is stored in computer programming.




# Writing methods and classes with Python

## First : Understanding Classes

1. Classes are templates for objects.

2. Classes combine state (data or variables) and behavior (methods) that apply to that data.

3. An object can be passed around and used in a program

## Class :
The relationship between classes and objects is like the relationship between a blueprint and a building. The blueprint defines where the walls should be, but the house is made of bricks and mortar. With a class, you can instantiate objects based on that blueprint. Those objects have the same structure.

But what’s actually in a class? 

A class contains state and behavior. State refers to data or variables. A Person class might have a “name” variable, for instance. A class’s behavior is simply a set of things that the class can do. This behavior is held in methods, which are identical in concept to functions.

## So what’s the difference between a method and a function?

A method is part of a class, while a function is independent of them. Methods can take parameters, modify the object's internal state, call other methods or functions, and return values. You “call” a function or method when you use it in code. For example, the line  x = add(2, 3)  calls the  add  function with the parameters 2 and 3.

Since a method is part of a class, it’s also part of an object that’s created from that class. The only difference between a function and a method is that methods are part of a class/object.

## Objects :

Unlike a class, which is just a template, an object is a real thing that can be passed around and used in our program. Objects can be stored in a variable, and the type of that variable is the class. Just like the type of the number “5” is an integer, and the type of the word “hello” is a string, the type of a customer object is Customer. We can modify the state of an object or call methods on it.We can instantiate multiple objects from the same class, and those objects are independent.

We can already create variables and make functions, why make classes and objects?

Object-oriented programming (OOP) is a different way of thinking about programming than the procedural programming you will have done before. OOP logically ties together data and the code that applies to that data.

## Second : Writing a Python Class 

1. Make a class using the  class  keyword.

2. The  __init__  method is known as the constructor.

3. Constructors are called when an object is created.

## Third : Creating Python Objects - Instantiate an Object

1. We can instantiate objects using their class’s name.

2. When We instantiate an object, we’re calling its constructor, and need to provide it the right parameters.

3. We can access and modify attributes, and call methods, using the  object.attribute  syntax.

4. Python deals with that for us! Remember that  self  just refers to  this object, and Python already knows what object we’re calling the method on. 


## Fourth : Appyling Inheritance in Python Code

1. A class can have a parent class or superclass.

2. The class with a parent is known as a subclass or child.

3. That class inherits attributes from its parent.

4. The child class can implement extra attributes on top of that which it inherits.


Why use Inheritance?

    1) Reusability
    The simplest reason is the same reason that you write functions - reusability.

    2) Extensibility
    Inheritance also allows for extensibility - i.e., the possibility of extending a program’s functionality without having to modify existing code. 

    3) Models
    They allow developers and development teams to build conceptual models of the behaviors and data in the system


 ## Fifth : Write a Subclass in Python - Define the Subclassing Syntax

1. Define a child class using  class Child(Parent).

2. By default, all classes inherit from an object - a Python object that provides basic functionality.

3. It’s possible for classes to inherit from multiple parent classes at once - in multiple inheritance.

## Sixth : Override Methods in Python - Understand Overriding

Overriding is when a child class creates a new implementation of an inherited method.

```
from abc import ABC
class Shape(ABC):
    def area(self):
        return 0
 
class Square(Shape):
    def __init__(self, length):
        self.length = length
 
    def area(self):
        return length * length
```

### Abstract Classes

So we get that `area()` is overridden, but how can Shape be a class? What’s ABC?

ABC stands for abstract base class. It’s Python’s mechanism for implementing what’s known as an abstract class.

An abstract class can’t be instantiated - the only way to use it is to create a subclass.       


### Accessing Parent Methods

While overriding allows you to entirely change inherited behavior, it’s sometimes useful to be able to access the parent’s methods - the ones that have been overridden.

One of the most common places to use this is in constructors. You do it using super() - like this: 

```
class Sprite:
    def __init__(self, image):
        this.image = image
 
    def render(self):
        pass
 
        class MovingSprite(Sprite):
    def __init__(self, image, speed):
        this.speed = speed
        super().__init__(image)
 
    def move(self):
        pass

```

In this example, MovingSprite is a subclass of Sprite, which moves an image rather than just rendering it in one place. All of the setup for the image and rendering part of the Sprite is done in the Sprite’s constructor, so MovingSprite calls the constructor after it’s done handling the  speed  parameter.

Couldn’t we just set  `this.image = image`  in MovingSprite’s constructor instead?

You could, but that solution doesn’t scale. Imagine if Sprite’s constructor did other operations to the image (like calculating its height and width) or imagine if MovingSprite got subclassed even further.

The `super()` approach allows you to reuse code rather than copying it, and ensures that functionality is grouped logically - two of the main benefits of object-oriented programming!

1. It’s possible for a child class to provide its own implementation for something it inherited from its parent.

2. The child’s implementation takes priority over the parent’s - it overrides the parent’s implementation.

3. Wou can use the super method to access methods in the parent class you’ve overridden.

4. An abstract class is a class that can’t be instantiated - it must be inherited from instead.


## Use Inheritance Hierarchies and Multiple Inheritance in Python

Multiple inheritance is more often than not an incorrect solution to your problem, but there are still some situations when it is still the best available.

Multiple inheritance involves one class having multiple parent classes. In an inheritance hierarchy, you have multiple levels of inheritance - where a class has a parent that has a parent.

Multiple inheritance has a bad reputation in object-oriented programming spaces - systems using it can be difficult to understand. Not only that, but some programming languages don’t implement it well, which causes problems.

Multiple inheritance is more often than not an incorrect solution to your problem, but there are still some situations when it is still the best available. In any case, you might run into multiple inheritance in the workplace, so we’ll cover it here.

```
Here’s an example:

class Cat:
    def meow(self):
        print(“Meow!”)
 
class Talker:
    def say(self, to_say):
        print(tosay)
 
class TalkingCat(Cat, Talker):
    pass
 
salem = TalkingCat()
salem.meow()
salem.say(“Hello!”)
```
Here you have a Cat class and a Talker class, both of which our TalkingCat class inherits from. That means that a TalkingCat, like our Salem here, can both meow and say things!

The pattern used here is often called a Mixin - because you “mix in” some required functionality. If you’ve programmed in other languages, you might be familiar with interfaces, traits, or typeclasses - which are similar but different concepts.

Wait, what happens if two parent classes implement the same method? Which one wins?

This is one of the main problems with multiple inheritance - called the diamond problem (or deadly diamond of death). Each language that uses multiple inheritance has a different solution - Python’s is called the MRO or Method Resolution Order.

Simply put, the MRO of a class is the order of places Python will look for a method definition. It can get quite complicated - and if you’re interested in more details, you can find them in the Python documentation.

Generally speaking, though, Python will look in the left-most parent class first. So in the TalkingCat example above, Python will look in Cat first, then Talker.

Apply Multiple Levels of Inheritance to a Python Program to solve the following problem :

Let’s assume that an image can either be a GIF or a JPG. Implement these subclasses of Image, then override the display method in each to also include a reference to what type it is.

## Problem :

It's the year 2000. You're working for a mobile phone company and have been tasked with modeling out the software for a cutting-edge phone that will have a built-in camera: a camera phone.

Create a class called Camera and a class called MobilePhone that will be the base classes of a derived class called CameraPhone. The CameraPhone class should be initialized with the memory attribute and should have a take_picture() method that prints out the message, Say cheese!.

The steps are as follows:

1. Create a Camera class with a take_picture() method that prints the message, "Say cheese!".

2. Create a MobilePhone class that will be initialized with a memory attribute.

3. Create a CameraPhone class that inherits from both the MobilePhone and Camera classes.

At the bottom of the script we have initialized an instance of the CameraPhone class and passed it the value "200KB". Then we call the take_picture() method and also print out the memory attribute.

## Using Collection of Objects - Lists and Dictionaries

1. You can store objects in collections - just like you can anything else.

2. The way Python deals with types is known as duck typing - if it looks like a duck and it quacks like a duck, it’s probably a duck.

3. When using collections, try not to access an object's attributes that it doesn't have. There are a variety of ways you can do that.

## Quiz:

Which of the following lines of code would allow you to call a parent class’s constructor from the child’s?


1. ParentClass()

2. ParentClass.__init__()

3. super()

4. super().__init__() # Right choice

## Objects are mutable because you can change their state.