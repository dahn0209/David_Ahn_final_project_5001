# Meeting Template

Go through this template in preparation for your meeting with the course staff member. We are not grading you on this template, just will help with questions and discussion. Please note, staff have the right to ask you to schedule a second meeting. The goal is to help you flesh out a reasonable project for this course, so make sure to use these meetings as a resource!

## Project Ideas
What are some ideas for your project? Why does that interest you?

* A password checker - this is more than just 'is this a good password or not', maybe checking against a dictionary, or checking against a list of known passwords, etc. Also calculations of difficulty or things like captcha's are good - so both checker and secure login system.
    * This interests me because I've worked on passwords input on React framework. Working on this will help me better implement password implementation for my personal web development projects
* Student Grading System/Applications
    * This interests me because I used to work with kids during my church internship and had to grade their process and works


## What are the big ideas?
How does this address some of the big learning ideas of 5001?
1.  The Password Checker
   *  Arithmetic Operators & Conditionals
      *  Use variables to store passwords, user inputs, and feedback messages
      *  Perform arithmetic operations to calculate password strength (e.g., length, diversity of characters).
      *  Use conditionals to enforce rules for password (e.x., containing at least one number").
   * Functions and Testing
     * Write reusable functions:
       * check_length(password)
       * contains_uppercase(password)
       * calculate_entropy(password)
     * Write unit tests for each function to verify correctness.
   * While Loops
      * Use a while loop to repeatedly prompt for a valid password until it meets all criteria.
      * Implement a retry system for failed login attempts.
   * Strings and Lists
     * Process passwords using string methods 
     * Use lists to store commonly used passwords or banned words for validation.
   * For Loops
     * Use for loops to iterate through password dictionaries for matching or validating.
     * Analyze each character in the password to calculate strength.
   * Computational Thinking
     * Break the problem into smaller components:
       * Password validation.
       * Checking against known weak passwords
       * User authentication flow.
   *  Recursion
      * Use recursion for CAPTCHA validation (e.g., "retry CAPTCHA if incorrect").
      * Implement recursive functions to generate potential password suggestions.
   * Error Handling
      * Handle invalid inputs gracefully using try-except blocks (e.g., non-string passwords).
      * Log errors for suspicious activity.
   * Dictionaries and Sets
      * Store banned passwords in a set for efficient lookup.
      * Use dictionaries to track login attempts ({'username': attempt_count}).
   * Classes and Objects
      * Create a  class to encapsulate all password-related methods.
      * Create a User class to manage user data, including encrypted passwords and login attempts.
   * Stacks and Queues
     * Use a stack for undoing recent password changes.
     * Use a queue for managing CAPTCHA challenges or login requests.
   * Searching and Sorting
     * Search for a password in a sorted list of known weak passwords using binary search.
     * Sort passwords by strength or creation date for administrative tools.

2. Student Grading System/Application
   * Variables, Arithmetic Operators & Conditionals
     * Use variables to store student details, grades, and averages.
     * Apply arithmetic operators to calculate grades, averages, and percentages.
     * Use conditionals for grade categorization (e.g., "A" for 90–100, "B" for 80–89).
   * Functions and Testing
     * Write reusable functions:
        * calculate_average(grades).
        * assign_grade(average).
        * add_student() and remove_student().
     * Test these functions using unittest to verify correctness.
   * While Loops
     * Use a while loop to create a menu-driven interface, e.g., "Add student," "View grades," or "Exit."
     * Allow repeated entry or editing of grades until the user chooses to stop.
   * Strings and Lists
     * Store student names and grades as strings.
     * Use lists to store multiple grades for each student.
     * Format strings for displaying results 
   * For Loops
     * Use for loops to iterate over students or grades when calculating averages or displaying data 
   * Computational Thinking
     * Divide the system into modules:
     * Data management (students and grades).
     * Calculations (averages, grades).
     * User interface (input/output).
     * Use problem-solving techniques for validation, data processing, and reporting.
   * Recursion
     * Implement recursion for advanced features, such as finding a student's rank in a recursive sorting algorithm.
     * Use recursion for navigating hierarchical menus.
   * Error Handling
     * Handle invalid inputs (e.g., non-numeric grades, duplicate student names) with try-except.
     * Prevent crashes by ensuring robustness in all user interactions.
   * Dictionaries and Sets
     * Use dictionaries to map student names to their grades:
  
        ```python
    
            students = {"Alice": [85, 90, 78], "Bob": [92, 88, 84]}

        ```
     * Use sets to manage unique subjects or class categories.
   * Classes and Objects
     * Create a Student class to encapsulate student details and methods (e.g., calculate_average()).
     * Create a Gradebook class to manage all students and their data.
   * Stacks and Queues
     * Use a stack for undo/redo functionality (e.g., undo grade edits).
     * Use a queue for managing grade entry or handling multiple classes in sequence.
   * Searching and Sorting
     * Implement search functionality to find a student by name or ID.
     * Sort students by average grades or alphabetical order.



## Code Design Thoughts
Are you including classes or APIs, what about dictionaries? One of the worst things you can do is go into a project assuming you are going to 'hard' code everything (this happens often with text based games, then students get stuck). You don't have to know details yet, but you should think about separation of concerns, and how to divide up your code. 

* The Password Checker will use classes and dictionaries
* The Student Grading System will use classes and dictionaries

## Resources Found
What are some resources you have found already or already have access to? (APIs, libraries, past assignments, etc)

Password Checker

https://www.geeksforgeeks.org/python-program-check-validity-password/
https://www.geeksforgeeks.org/password-validation-in-python/
https://www.javatpoint.com/password-validation-in-python   
https://github.com/virgoaugustine/Password-Checker?tab=readme-ov-file 
https://medium.com/@michaellopezcs17/creating-a-simple-password-strength-checker-in-python-30656096ade8
https://www.youtube.com/watch?v=q5uM4VKywbA


Student Grading System/Application

https://samywrites.hashnode.dev/building-a-grading-system-in-python-a-step-by-step-guide

https://www.geeksforgeeks.org/program-create-grade-calculator-in-python/
https://github.com/LazarosPan/Student-Grade-Management-System




## Timeline
Setup a general timeline that includes research and development, and when you want to have certain aspects of the project done. 

1. 11/22: Getting Schema Design, relationships between data and information, and Research done
2. 11/29: Get Development Done 
   1. Check password is viable(11/26) teriminal interface necesary (11/29) - 
   2. saves CSV files (11/30)
   3. multiple user loginning in 
3. 12/1: Get Draft done and reviewed (12/2)
4. 12/5: Get Final Code Finished 


## Priority
- organized to minium viable product
  - individual features that can be added one at a time. 
  - indepedent feature
  -Minimum viable parts: checking whether it is a valid password or not?
 - Saving password data in CSV file
 - Unit Testing: write code in ways it can be tested
   - doctest
   - unit test
  





  - CRUD- user can login, sign up, update
 