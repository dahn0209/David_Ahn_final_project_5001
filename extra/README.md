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

### 1. Install Dependencies:
Make sure you  have the necessary Python libraries installed. Specifically, this project uses the bcrypt library for password hashing. To install it, you can use pip:

```bash
pip3 install bcrypt
```
### 2. Running the code

Execute the main.py file since it's the main entry point of the program.This will launch the interactive menu.

In your terminal or command prompt, navigate to the project directory and run:

```bash
python3 main.py
```
### 3. Using the Application

After running main.py, a menu pops out of the terminal with options such as setting a database, signing up, and managing users. 

```
User System
1. Set User Database
2. Create New User Database
3. View Current Database
4. Sign Up
5. Sign In
...
1.  Exit

```
To navigate the menu,
* Enter the number corresponding to the menu option.
* Follow on-screen prompts for inputs (e.g., usernames, passwords, or database names).
### 4. Example of Interaction
  1.  Setting User Database csv file
      * Select option 1 from the menu
      * Enter the existing CSV file to use  
```
User System
1. Set User Database
2. Create New User Database
3. View Current Database
4. Sign Up
5. Sign In
6. Sign Out
7. Update Password
8. Delete User
9. Delete User Database
10. Get Current User
11. Exit
Choose an option: 1
Enter the existing CSV file to use: user_db.csv
User database set to 'user_db.csv'.

```
  2. Sign Up a New User:
    * Select option 4 from the menu.
    * Enter a username and a strong password that satisfies the rules.
```
User System
1. Set User Database
2. Create New User Database
3. View Current Database
4. Sign Up
5. Sign In
6. Sign Out
7. Update Password
8. Delete User
9. Delete User Database
10. Get Current User
11. Exit
Choose an option: 4
Enter username: john_doe
Enter password: SecurePassword123!
Sign up successful!
```
  3. Sign In:
     * Select option 5.
     * Provide the same username and password.  
```
User System
1. Set User Database
2. Create New User Database
3. View Current Database
4. Sign Up
5. Sign In
6. Sign Out
7. Update Password
8. Delete User
9. Delete User Database
10. Get Current User
11. Exit
Choose an option: 5
Enter username: john_doe
Enter password: SecurePassword123!
Current signed-in user: john_doe
```
 1. Sign Out:
     * Select option 6.
     * user is signed out.  
```
User System
1. Set User Database
2. Create New User Database
3. View Current Database
4. Sign Up
5. Sign In
6. Sign Out
7. Update Password
8. Delete User
9. Delete User Database
10. Get Current User
11. Exit
Choose an option: 6
User 'john_doe' signed out successfully!
```

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

### 1. Environment
* Install Python  

```
python3 --version

```  
* Install bcrypt for hashing

```
pip3 install bcrypt

```

### 2. Database
*   Make sure USER_DB.csv exist. If it does not:
    *   Create it manually and includes username and password as header
    *   Initalize it by running initalize_user_db()

### 3. Run the Code
* Run main.py to run the code directly
  ```
  python3 main.py

  ```
### 4. Testing

* To run doctest, run the specific file (eg. auth.py) with a doctest

```
python -m doctest -v auth.py

```

* To run unit test, run the test files in the tests foldler

```
cd tests
python3 test_main.py
```

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### 1. auth.py - Authentication and Password Hashing

Password Hashing securely hashes the password before storing it in the database with bcrypt.Password Verification compares input passwords with the hashed version stored in the database.

   * hash_password() takes a plain-text password, generates a salt using bcrypt.gensalt(), and returns the hashed password. It ensures the password is not empty before processing.
  
   ```python 
   def hash_password(password):
    if not password:
        raise ValueError("Password cannot be empty.")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
   ```

   * check_password() veritfies whether a given password matches the hashed password stored in the database using bcrypt.checkpw. It also includes  error handling for invalid input types.
  
   ```python
   def check_password(hashed_password, password):
    if hashed_password is None:
        raise TypeError("Hashed password cannot be None.")
    if not isinstance(hashed_password, bytes):
        raise ValueError("Hashed password must be in byte format.")
    if password is None or password == "":
        raise ValueError("Password cannot be empty.")
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
   ```

### 2. database.py - Database Management 

Database Initialization creates and initializes the user database  in a CSV file. Database Operations allows users to switch databases, create new ones, and delete them.

* set_user_db() selects which CSV file to use as the user database.

```python 
def set_user_db(file_name):
    global USER_DB
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    USER_DB = file_name
    return f"User database set to '{file_name}'."

```
* initialize_user_db() initializes the user database by creating a CSV file with headers if it doesn’t exist.
  
```python
def initialize_user_db():
    db_file = global_change_db()
    if not os.path.exists(db_file):
        with open(db_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])

```

### 3. main.py - Command-Line User Interface

An Interactive Menu provides a user-friendly terminal-based menu for interaction. User Account Management integrates all features such as sign-up, sign-in, and database management.Streamlined Navigation maps out each menu option to its respective functionality.

  * display() presents options to users for interacting with the system.

```python

def display():
    print("\nUser System")
    print("1. Set User Database")
    print("2. Create New User Database")
    ...
    print("11. Exit")

```
  * choices() routes user to the appropiate function based on the menu selection. 

```python

def choices(choice):
    try:
        if choice == "1":
            new_db = input("Enter the existing CSV file to use: ")
            print(set_user_db(new_db))
        elif choice == "2":
            new_db_name = input("Enter the name of the new user database: ")
            print(create_new_user_db(new_db_name))
        ...
        elif choice == "11":
            print("Goodbye!")
            return False
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
    return True

```

### 4. user_management.py - User Account Operations

Sign-Up and Sign-In help allow for new user registration and authentication. Session Management helps track the currently logged-in user. Password Updates allows users to  update their passwords.
Account Deletion allows users to delete their accounts.

  * sign_up()  validates the password using functions imported from utils.py, checks for duplicate usernames in the current csv file, and adds the new user with a hashed password in the csv file.
  
  ```python
  def sign_up(username, password):
    initialize_user_db()
    db_file = global_change_db() 
    try:
        is_valid_password(password)
    except ValueError as e:
        return str(e)

    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'].lower() == username.lower():
                return "Username already exists."

    hashed_password = hash_password(password)
    with open(db_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username.lower(), hashed_password.decode('utf-8')])

    return "Sign up successful!"

  ```
  * sign_in() authenticates a user by matching the provided password with the stored hashed password in the csv file.

  ```python 
  def sign_in(username, password):
    global current_user
    db_file = global_change_db() 
    if current_user is not None:
        return f"Error: User '{current_user}' is already signed in."

    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                if check_password(row['password'].encode('utf-8'), password):
                    return set_username(username)
                else:
                    return "Invalid password."
    return "Username not found."
  ```

### 5. utils.py - Password Utilities

Password Validation enforces password strength rules such as password length, special characters, numbers, and captialization.
Password Reuse Check impedes users from reusing existing passwords in the csv file.

  * is_valid_password() enforces rules for passwords (e.g., length, character types, no spaces) and ensures it is not reused.
  
  ```python 
  def is_valid_password(password):
    if len(password) <= 8:
        raise ValueError("Password must be more than 8 characters.")
    if len(password) > 20:
        raise ValueError("Password must be less than 20 characters.")
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValueError("Password must contain at least one special character.")
    if re.search(r"\s", password):
        raise ValueError("Password must not contain spaces.")

    if is_password_reused(password):
        raise ValueError("Password is already in use by another account.")

    return True

  ```
  * check_password() validates a password against its hashed version using bcrypt.checkpw. 
  
  ```python
  def check_password(hashed_password, password):
    if hashed_password is None:
        raise TypeError("Hashed password cannot be None.")
    if not isinstance(hashed_password, bytes):
        raise ValueError("Hashed password must be in byte format.")
    if password is None or password == "":
        raise ValueError("Password cannot be empty.")
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

  ```

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
### Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

Due to time constraints, I did not have the chance to implement other password checker methods such as password strength ratings, captcha, and entropy to improve password security. However, I was too focused on username implementation and learning CSV file implementations for this project. If I had more time, I would like to implement email verification, and two-factor authentication to increase security checks. 


## Final Reflection
### Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

CS5001 was important because it helped me comprehend the fundamentals of Python and put it into practice. Learning JavaScript in the past helped with the learning process because there were many topics such as strings, loops, variables, and functions that crossover. However, some differences convoluted me many times such as global variables, mutable and immutable data, and Recursion However, practice problems from HW, and team review sessions helped me comprehend the topics for this course. To learn and improve, I need to do more practice problems with Python involving Recursion, Stack, Queue, Searching, and Sorting to become a better programmer and make codes with efficient Time and Space Complexity. My key takeaway from this course is that everything in Software Engineering is cumulative and so I will always be practicing what I learn in this class in future classes. Practicing, Teamwork, and Asking for Help are important for learning and becoming a better programmer. 