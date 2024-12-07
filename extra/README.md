# Final Project Report

* Student Name: David Ahn
* Github Username: Dahn0209
* Semester: Fall 2024
* Course: CS 5001


## Description 
### General overview of the project, what you did, why you did it, etc.

The Final Project is a simplified user management system with sign-up, sign-in, password management, and user management features. It relies on a CSV file as the user database to save the data, which stores usernames and hashed passwords. Passwords are hashed using bcrypt to enhance security, and the system checks password strength and reusability to prevent weak or reused passwords.

I decided to create this project because this project will complement and improve my previous experience working on e-commerce websites dealing with user sign-up and sign-in with passwords from my bootcamp projects. Rather than using JavaScript and JavaScript frameworks such as React, Node, and Express, I wanted to implement Python and other new tools for coding. During my Final Project discussion, I was still brainstorming about database storage. Reflecting on previous homework such as HW 7 and HW 8, I thought JSON files were ideal for saving data. However, the TA recommended that I use CSV files for storing data. Thus, 

I researched more about CSV, and other examples of password checkers to help me create a project that saves usernames and passwords into different files with sign-up, sign-in, password management, and user management features.


## Key Features
### Highlight some key features of this project that you want to show off/talk about/focus on. 

#### Secure Password Authentication:
bcrypt creates hashed passwords for secure storage and verification.This secure password validation and authentication ensures users create strong, secure passwords that meet established criteria.

#### User Management:

User Management includes a system that involves user creation, login, password updates, deletion, and sign-out. Users can manage the current signed-in user through different operations

#### Database Management:

The system uses a CSV file to store user data (username, hashed password). It provides options for setting, creating, and deleting databases. It can easily initialize user database if it doesn't exist.

#### Password Reuse Prevention:

It checks whether passwords were reused across user accounts to prevent users from selecting passwords they’ve used previously.

#### Command-Line Interface:

It provides a simple and interactive CLI for users to manage their accounts and interact with the user database.

#### Extensibility and Flexibility:

The system opens the possibility of adding additional functionality such as email verification, and two-factor authentication in the future.
It allows working with multiple databases such as the set_user_db() function, which allows flexibility in managing user accounts.





## Guide
### How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

1. #### Install Dependencies:
Make sure you  have the necessary Python libraries installed. Specifically, this project uses the bcrypt library for password hashing. To install it, you can use pip:

```bash
pip3 install bcrypt
```
2. #### Running the code

Execute the main.py file since it's the main entry point of the program.This will launch the interactive menu.

In your terminal or command prompt, navigate to the project directory and run:

```bash
python3 main.py
```




## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.