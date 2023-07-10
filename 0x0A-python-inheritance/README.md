# Python - Inheritance
* Introduction
Inheritance is a powerful feature in object-oriented programming that allows classes to inherit properties and behaviors from other classes. In Python, inheritance is implemented using the concept of superclass (parent class) and subclass (child class).

# Basic Concepts
Inheritance allows a subclass to inherit attributes and methods from a superclass. The subclass can extend the functionality of the superclass by adding new attributes or overriding existing methods. This promotes code reusability and modularity.

* Defining Subclasses
To create a subclass, you define a new class and specify the superclass it inherits from using parentheses and the superclass name. 

# Overriding Methods
A subclass can override methods inherited from its superclass by redefining them within the subclass. This allows the subclass to provide its own implementation of the method.

# Multiple Inheritance
Python supports multiple inheritance, which means a subclass can inherit from multiple superclasses. In the case of conflicts, the method resolution order (MRO) determines which method is invoked.

# Best Practices
1. Use inheritance to promote code reuse and create logical class hierarchies.
2. Make sure the subclass "is-a" type of the superclass to maintain the principle of object-oriented programming.
3. Avoid excessive deep inheritance hierarchies, as they can lead to complexity and maintenance issues.
4. Override methods when necessary, but be mindful of maintaining the expected behavior defined in the superclass.
5. Use meaningful and descriptive class names to enhance code readability.
