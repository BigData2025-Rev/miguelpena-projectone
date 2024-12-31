# ProjectOne - PokeMart

## Description
PokeMart is a storefront that allows users to exchange dollars to PokeDollars, and purchase items like Pokeballs, MaxRevives, etc. An admin can view and manage the inventory, add and remove users, view and modify orders, grant admin access to users.     

## Application Requirements
Create a Python application that connects to either a MySQL or MongoDB server,
and performs CRUD operations on a database. The application should model a store,
where users can create accounts, purchase products, and look at a history of their
orders. There should also be an admin feature where the admin should be able to 
see all orders and users. 

    - The application must be able to create, read, update, and delete.
    - Use at least 3 different tables/collections (also create an ERD)
    - The application must have a login feature, as well as user/admin roles
    - Logging of events should be implemented (connecting to db, interacting with db/files, etc.)

Your "store" can be whatever you want (furniture, appliances, movies, etc.). Some 
admin features that you may want to implement: modifying inventory, removing/editing users,
granting admin access to specific users...

## Presentation:
    We will present our projects the morning of January 10, 2025.
    Short ~3-5 minute demonstration of all the functionalities of your project.
    Please create a short slide show that explains the project and tech stack.
    The bulk of the presentation will be demonstrating the application itself.

## Tech Stack
- Python
    - BCrypt Module -> For password hashing.
        - pip install bcrypt
    - Maskpass Module -> For password hiding.
        - pip install maskpass
    - pymongo -> for CRUD of inventory information
    - mysql.connector -> for CRUD of user accounts, balance, orders.
    - CSV or JSON Module -> For saving/loading data
    - Matplotlib Module -> For displaying data
        - pip install matplotlib
    - Pandas Module -> For organization of data
        - pip install pandas
    - tkinter -> display storefront with inventory images.
- Git (+ Github)
