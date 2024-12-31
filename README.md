# Project0 - BudgetBuddy

A Python CLI (Command Line Interface) application that saves and reads data from a JSON file. It is a budgeting app that keeps track of spenditure and displays historical data. 
The user is prompted to create a profile and provide a monthly income value. Every time the user spends money, they are encouraged to enter it into this application and give it a category.
The application then displays their largest category and how they spend.   

## Application Requirements
- CLI where users can interact with the application while it is running
- Application should read in data from a file and be displayed in some way
- Application should write data to a file
- All user input should be validated (program should not end with exceptions based on user input)
- Program must follow OOP design (classes/objects)
- Application should be uploaded to a GitHub repository

## Tech Stack
- Python
    - BCrypt Module -> For password hashing.
        - pip install bcrypt
    - Maskpass Module -> For password hiding.
        - pip install maskpass
    - CSV or JSON Module -> For saving/loading data
    - Matplotlib Module -> For displaying data
        - pip install matplotlib
    - Pandas Module -> For organization of data
        - pip install pandas
- Git (+ Github)
