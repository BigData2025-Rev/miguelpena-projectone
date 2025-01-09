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
    - Passlib -> For password hashing.
        - pip install passlib
    - BCrypt Module -> For password hashing.
        - pip install bcrypt
    - Maskpass Module -> For password hiding.
        - pip install maskpass
    - pymongo -> for CRUD of inventory information
        - pip install pymongo
    - mysql.connector -> for CRUD of user accounts, balance, orders.
        - pip install mysql-connector-python
    - CSV or JSON Module -> For saving/loading data
    - Matplotlib Module -> For displaying data
        - pip install matplotlib
    - Pandas Module -> For organization of data
        - pip install pandas
    - tkinter -> display storefront with inventory images.
    - Flask -> for API development
        - pip install flask
    - Flask Restful -> for developing RESTful API with Flask
        - pip install flask-restful
    - SQLAlchemy -> for ORM (object relational mapping) with SQL database.
        - pip instal sqlalchemy
    - Flask SQLAlchemy -> simplified usage of SQLAlchemy with Flask
        - pip install -U Flask-SQLAlchemy
    - Flask Marshmallow -> simplified validation for endpoints
        - pip install flask-marshmallow
    - Flask JWT Extended -> simplified authorization tokens
        - pip install flask-jwt-extended
    - dotenv -> for loading .env files with environment variables.
        - pip install python-dotenv
- Git (+ Github)

## Project Documentation

The project is seperated between a frontend and a backend. The backend will handle everything that has to do with the database management, and provide an RESTful API to which the frontend can make requests. The frontend will be the CLI application that takes in User input and makes requests to the backend for database CRUD operations. 

### The Backend

This will be a RESTful API with the respective GET, POST, PUT, PATCH, and DELETE methods for CRUD operations on a MySQL Database and MongoDB Database.

The API is built with Flask-Restful module, which makes it easy to build a Restful API. Along with object relational mapping (ORM) with SQLAlchemy, Flask-SQLAlchemy will simplify CRUD operations to a MySQL database. It automatically creates the tables with the appropriate constraints, and makes join operations easier to do. The only one that will be from scratch will be when interfacing with MongoDB with pymongo.

The database tables and collections will be the following:

MySQL:
    - Accounts
        - ID
        - Username
        - Email
        - Password (Hashed)
    - Account Details
        - ID
        - Account ID
        - First Name
        - Last Name
    - Balance
        - ID
        - Account ID
        - Amount
    - Orders
        - ID
        - Account ID
        - Item ID
        - Qty
        - TimeStamp
    - Item Categories
        - ID
        - Name
    - Item Simplfied
        - ID
        - Name
        - Cost
        - Category ID

MongoDB:
    - Item Complicated
        - Item ID
        - Item Name
        - Item Cost
        - Item Image URL
        - Item Description

The MySQL tables are in 3NF forms for referential integrity. The MongoDB collection is primarily for storage of more complicated data like a description which can be more than 255 characters long, and a URL for the image. The name and cost are for sanity checks between the MySQL tables and MongoDB collection.

Logging will occur here.


### The Frontend

This will be a CLI application that can take in input from a user. It will handle creation of accounts, logging in, admin features, and store interaction by interfacing with the RESTful API of the backend.

It will display the store items upon request by the user. 

It will display order history and statistics upon request as well.

Admins will be able to assign Admin role to users, add/remove/modify/view inventory items, and see all orders.

Some stretch goals:
    - Have a tkinter window popup that displays the item images if it has one.
    - Allow users to request a refund, and return the item.
    - Allow users to view their balance and inventory.
    - Allow admins to cancel and order and refund the user. 