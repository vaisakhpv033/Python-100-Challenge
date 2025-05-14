# Python-100-Challenge

Welcome to this collection of Python programming challenges! This list is designed to help you practice and enhance your Python skills, ranging from fundamental concepts to more advanced topics. The questions are organized by increasing complexity, allowing for a progressive learning experience.

Happy Coding!

## Section 1: Python Fundamentals & Basic Data Structures

This section covers foundational Python concepts, basic data types, string and list manipulations, and simple functions.

1.  **Generating a Random Number**: Write a Python function that generates and returns a random integer within a specified range (e.g., between 1 and 100, inclusive).
2.  **Generating a 6-Digit Random OTP**: Write a Python function that generates a random 6-digit One-Time Password (OTP) consisting of digits (0-9). The OTP should be returned as a string.
3.  **Lambda to Generate Random Number**: Write a Python lambda function that, when called, returns a random integer between a specified minimum and maximum value (inclusive).
4.  **Extracting Digits from a String**: Write a Python function that takes a string as input and returns a new string containing only the digit characters present in the original string, preserving their order.
5.  **Sum of Digits in a Number**: Write a Python function that takes an integer as input and returns the sum of its digits.
6.  **String Manipulation**: Demonstrate various string manipulation techniques in Python by performing the following operations on a given string:
    * Concatenate it with another string.
    * Replace a specific substring with another substring.
    * Change the case of the string (e.g., to uppercase or lowercase).
    * Remove specific characters or substrings.
    * Split the string into a list of substrings based on a delimiter.
7.  **Reversing a String by Words**: Write a Python function that takes a string as input and returns a new string where the order of the words in the original string is reversed.
8.  **Removing Duplicates from a List**: Write a function that takes a list as input and returns a new list containing only the unique elements from the original list, preserving the original order if possible.
9.  **Slicing a List for Halves**: Write a Python function that takes a list as input, divides it into two roughly equal halves, and returns these two halves as a tuple of lists.
10. **Filtering Odd Numbers with Lambda**: Given a list of numbers, use the `filter()` function along with a lambda function to create a new list containing only the odd numbers from the original list.
11. **List Comprehension for Squaring/Cubing**: Given a list of numbers, use a list comprehension to create a new list where each even number from the original list is squared, and each odd number is cubed.
12. **Dictionary Workouts**: Create a series of short practical exercises involving dictionaries, such as:
    * Creating a dictionary.
    * Accessing values.
    * Adding and updating key-value pairs.
    * Deleting key-value pairs.
    * Iterating through keys, values, and items.
    * Checking for key existence.
13. **Enumerating a Dictionary**: Write a Python loop that iterates through the key-value pairs of a dictionary and prints both the index (count) and the key-value pair for each item.
14. **Dictionary Keys to Tuple**: Write a Python function that takes a dictionary as input and returns a tuple containing all the keys of the dictionary.
15. **Capitalizing Dictionary Keys**: Write a Python function that takes a dictionary as input and returns a new dictionary where all the keys of the original dictionary are capitalized (converted to uppercase).
16. **Safe Key Value Check in Dictionary**: Write a Python function that takes a dictionary and a key as input. It should check if the key exists in the dictionary and if its corresponding value is not `None` (or some other specific value) without using a `try-except KeyError` block. Return `True` if the key exists and the value meets the condition, and `False` otherwise.
17. **Combining Tuples Without `+`**: Write a Python function that takes two or more tuples as input and returns a new tuple that is the concatenation of all the input tuples, without using the `+` operator for concatenation.
18. **Printing Current Time**: Write a Python script that prints the current time in a human-readable format. *Assume the current location is Kochi, Kerala, India.*
19. **Getting Tomorrow's Date**: Write a Python function that returns the date of the day after the current date. The output should be in a standard date format (e.g., `YYYY-MM-DD`). *Assume the current date is May 14, 2025, in Kochi, Kerala, India.*
20. **Date 15 Days Before Today**: Write a Python function that calculates and returns the date that was 15 days prior to the current date. The output should be in a standard date format (e.g., `YYYY-MM-DD`). *Assume the current date is May 14, 2025, in Kochi, Kerala, India.*
21. **Number of Days Between Two Dates**: Write a Python function that takes two dates (as strings in a specific format or as date objects) as input and returns the number of days between them as an integer.
22. **Counting Days Between Two Dates (Format Specific)**: Write a Python function that takes two dates as input (in a consistent format like 'YYYY-MM-DD') and returns the absolute difference in days between them.

## Section 2: Intermediate Data Structures & Functions

This section delves into more complex manipulations of data structures, function design, and introductory object-oriented concepts.

23. **Removing Dictionary Items by Value**: Write a function that accepts a dictionary and a target value as input. The function should return a new dictionary containing only the key-value pairs from the original dictionary where the value is not equal to the target value. Alternatively, modify the original dictionary in-place to remove such items.
24. **Most Repeated Letter in String**: Write a Python function that takes a string as input and returns the letter that appears most frequently in the string. Ignore case and consider only alphabetic characters. If there's a tie, you can return any of the most frequent letters.
25. **Second Largest Number in List**: Write a Python function that takes a list of numbers as input and returns the second largest number in the list. Handle cases where the list has fewer than two elements or contains duplicates.
26. **Check Digit Repetition in Number**: Write a Python function that takes an integer as input and returns `True` if any digit repeats within the number, and `False` otherwise.
27. **Swap First and Last Digits of Number**: Write a Python function that takes an integer as input and returns a new integer where the first and last digits of the original number have been swapped. Handle cases for single-digit numbers.
28. **Alternating Case in String**: Write a Python function that takes a string as input and returns a new string where the case of the characters alternates (e.g., "hello" becomes "HeLlO" or "hElLo").
29. **List of Dicts to List of Values**: Write a function that takes a list of dictionaries and a key as input. The function should return a new list containing the values associated with that specific key from each dictionary in the input list. Handle cases where a dictionary might not contain the specified key (e.g., by skipping it or returning a default value).
30. **List Comprehension with Conditions**: Use list comprehension to solve problems like:
    * Creating a new list containing only the even numbers from an existing list.
    * Creating a new list containing the squares of numbers from an existing list that are greater than 5.
    * Applying a transformation to elements based on a condition.
31. **Interchange Keys and Values in Dictionary**: Write a function that takes a dictionary as input and returns a new dictionary where the original keys are now the values and the original values are now the keys. Assume the original values are hashable.
32. **Combining Dictionaries (Summing Common Keys)**: Write a function that takes two dictionaries as input. It should return a new dictionary that contains all the keys from both input dictionaries. If a key exists in both dictionaries, the corresponding values should be added together in the new dictionary. If a key exists in only one dictionary, its value should be included as is in the new dictionary.
33. **Find and Remove Key for Lowest Value**: Write a Python function that takes a dictionary as input, finds the key associated with the minimum value in the dictionary, removes that key-value pair from the dictionary (in-place modification), and returns the removed key.
34. **Function for N Prime Numbers**: Write a Python function that takes an integer `n` as input and returns a list containing the first `n` prime numbers.
35. **Second Largest Odd Number in List**: Write a Python function that takes a list of numbers as input and returns the second largest odd number in the list. Handle cases where there are fewer than two odd numbers.
36. **Importing Functions Between Files**: Create two Python files (`module1.py` and `main.py`). In `module1.py`, define one or more functions. In `main.py`, import these functions from `module1.py` and call them to demonstrate their usage.

## Section 3: Advanced Topics, OOP & Decorators

This section explores advanced Python features, including object-oriented programming principles, decorators, generators, and complex data manipulations.

37. **Basic Bank Account Class**: Define a Python class named `BankAccount` with the following:
    * Attributes: `name` (string) and `balance` (numeric).
    * Methods:
        * `deposit(amount)`: Adds the given amount to the balance.
        * `withdraw(amount)`: Subtracts the given amount from the balance. Ensure there are sufficient funds before withdrawal.
        * `check_balance()`: Returns the current balance.
38. **Class Initialization and Method Usage**: Define a Python class that takes arguments in its `__init__` method and stores them as instance attributes. Then, create a method within the class that uses these stored attributes to perform some operation and return a result.
39. **Generators for Sequential Values**: Write a Python generator function that yields a sequence of values (e.g., numbers or strings). Demonstrate how to create an iterator from this generator and print the first two or three items yielded by the generator individually using `next()`.
40. **Summing Integers in Nested Dictionary**: Given a dictionary that may contain values of different types (including nested dictionaries and other data types), write a function to calculate and return the sum of all integer values found within the dictionary (and any nested structures).
41. **Extracting URL Components (String Manipulation)**: Write a Python function that takes a URL string as input and attempts to extract and return its main components (e.g., scheme, hostname, path) as a dictionary or a tuple. Use string manipulation techniques (without relying heavily on built-in URL parsing libraries for this exercise).
42. **Dictionary Comprehension**: Use dictionary comprehension to solve problems like:
    * Creating a new dictionary by swapping keys and values of an existing dictionary (assuming unique values).
    * Creating a new dictionary by filtering key-value pairs based on a condition.
    * Creating a new dictionary by applying a transformation to keys or values.
43. **Filter List of Dictionaries by Missing Key**: Given a list of dictionaries, write a list comprehension or a function that returns a new list containing only the dictionaries that *do not* have a specific key.
44. **Sort List of Dictionaries by Key**: Given a list of dictionaries, write a Python function that sorts the list based on the values associated with a specified key in each dictionary. You should be able to specify whether the sorting should be in ascending or descending order.
45. **Create Class Instances from List of Dictionaries**: Given a list of dictionaries, where each dictionary contains data relevant to the attributes of a class you define (e.g., a `Person` class with 'name' and 'age' keys), write a Python function that iterates through the list of dictionaries and creates an instance of your class for each dictionary, initializing the instance attributes with the dictionary values. Return a list of these created class instances.
46. **Variadic Function for Sum and Average**: Write a Python function that accepts any number of numerical arguments. The function should calculate and return both the sum and the average of these arguments. Include type checking to ensure all arguments are numbers.
47. **Decorator Workout**: Create one or more practical examples of Python decorators. These examples should demonstrate how decorators can modify the behavior of functions, such as adding logging, timing execution, or enforcing argument types.
48. **Decorator to Convert Int Output to String**: Write a Python decorator that, when applied to a function that returns an integer, modifies the function's behavior to return the integer as a string instead.
49. **Decorator to Prepend String**: Write a Python decorator that takes a string as an argument. When this decorator is applied to a function, it modifies the function's output (if it's a string) by prepending the decorator's string argument to it.
50. **Flattened to Nested Dictionary**: Given a dictionary where keys are strings representing a path (e.g., 'a.b.c'), write a function to convert it into a nested dictionary structure. For example, `{'a.b.c': 42, 'a.d': 10, 'e': 5}` should become `{'a': {'b': {'c': 42}, 'd': 10}, 'e': 5}`.
51. **Advanced OOP: Properties, Destructor, Super()**:
    * Define a base class and a derived class.
    * Demonstrate how the derived class can access and use properties of the base class in its methods.
    * Implement a `__del__` (destructor) method in one of the classes and explain when it is called.
    * Define and use a class property (a variable shared by all instances of the class).
    * Define and use a property method (`@property`, `@setter`) to control attribute access.
    * Show how the `super()` function is used in the derived class to call methods (including `__init__`) of the base class.
