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
    - Backend:
        - Flask -> for API development.
        - Flask Restful -> for developing RESTful API with Flask.
        - SQLAlchemy -> for ORM (object relational mapping) with SQL database.
        - Flask SQLAlchemy -> simplified usage of SQLAlchemy with Flask.
        - Flask Marshmallow -> simplified validation for endpoints.
        - Flask JWT Extended -> simplified authorization tokens.
        - dotenv -> for loading .env files with environment variables.
        - pymongo -> for CRUD of inventory information.
        - mysql.connector -> for CRUD of user accounts, balance, orders.
        - Passlib -> For password hashing.
    - Frontend:
        - Requests -> For making HTTP requests.
        - Maskpass Module -> For password hiding.
        - Pandas Module -> For organization of data.
        - tkinter -> display storefront with inventory images.
- Git (+ Github)

## Dependencies

- pip install flask
- pip install flask-restful
- pip install sqlalchemy
- pip install -U Flask-SQLAlchemy
- pip install flask-marshmallow
- pip install flask-jwt-extended
- pip install python-dotenv
- pip install passlib
- pip install requests
- pip install maskpass
- pip install pymongo
- pip install mysql-connector-python
- pip install pandas
- pip install tkinter
- pip install tqdm

## Project Documentation

The project is seperated between a frontend and a backend. The backend will handle everything that has to do with the database management, and provide an RESTful API to which the frontend can make requests. The frontend will be the CLI application that takes in User input and makes requests to the backend for database CRUD operations. 

### The Backend

This will be a RESTful API with the respective GET, POST, PUT, PATCH, and DELETE methods for CRUD operations on a MySQL Database and MongoDB Database.

The API is built with Flask-Restful module, which makes it easy to build a Restful API. Along with object relational mapping (ORM) with SQLAlchemy, Flask-SQLAlchemy will simplify CRUD operations to a MySQL database. It automatically creates the tables with the appropriate constraints, and makes join operations easier to do. The only one that will be from scratch will be when interfacing with MongoDB with pymongo.

The database tables and collections will be the following:

MySQL:
    - Accounts
        - ID (PK)
        - Username
        - Email
        - Password (Hashed)
    
    - Profiles
        - ID (PK)
        - First Name
        - Last Name
        - Age
        - Favorite Pokemon

    - Account_Profiles [Composite Key Relational Table for 3NF]
        Account_Id (FK)
        Profile_Id (FK)

    - Balance
        - ID (PK)
        - Amount

    - Account_Balances [Composite Key Relational Table for 3NF]
        Account_Id (FK)
        Balance_Id (FK)

    - Orders
        - ID (PK)
        - Account ID (FK)
        - Item ID (FK)
        - Qty
        - Total
        - Created_on 

    - Item_Categories
        - ID (PK)
        - Name 
        - SLUG 

    - Items
        - ID (PK)
        - Name
        - Detail_ID (pyMongo _id for item description and image)
        - Cost
    
    - Item_Category_Relational [Composite Key Relational Table for 3NF]
        - Item_Id (FK)
        - Item_Category (FK)

MongoDB:
    - Items
        - Item ID (Store in MySQL for quick queries)
        - Item Name
        - Item Cost
        - Item Image URL
        - Item Description

The MySQL tables are in 3NF forms for referential integrity. The MongoDB collection is primarily for storage of more complicated data like a description which can be more than 255 characters long, and a URL for the image. The name and cost are for sanity checks between the MySQL tables and MongoDB collection.


### The Frontend

This will be a CLI application that can take in input from a user. It will handle creation of accounts, logging in, admin features, and store interaction by interfacing with the RESTful API of the backend.

For each request, the app should include an access_token in the header section of the request. e.g., Authentication='TokenString' which is a secure way of ensuring that only admins have access
to specific endpoints, like DELETE on /pokemart/items.

It will display the store items upon request by the user. 

It will display order history and statistics upon request as well.

Admins will be able to assign Admin role to users, add/remove/modify/view inventory items, and see all orders.

The CLI app should log every response it recieves from the API, and handle errors accordingly.

Some stretch goals:
    - Have a tkinter window popup that displays the item images if it has one.
    - Allow users to request a refund, and return the item.
    - Allow users to view their balance and inventory.
    - Allow admins to cancel and order and refund the user. 

# User Stories

"As a user I should be able to create an account by choosing a username, entering a password, 
and providing details like my first and last names, age, and favorite pokemon." 
    Backend:
        - The api should have an endpoint /auth/register where an app can POST a username and password.
        - The api should hash the password before storing on a database, and it should perform validation.

    Frontend:
        - The CLI app should get input from a user and POST the gathered info to the /auth/register endpoint.
        - The CLI app should then handle authentication tokens for the user, abstracting it all away.
        

"As a user I should be able to login immediately after creating an account, and access PokeMart."
    Backend:
        - The api should have an endpoint /auth/login where an app can POST a username and password.
        - The api should check the provided username, and see if it matches a username on the database.
        - The api should check the provided password and see if it matches to the stored hashed password,
        - The api should return authentication tokens in the response when a successful login occurs.
    Frontend:
        - The CLI app should get input from a user, validate, and POST the gathered info to the /auth/login endpoint.
        - The CLI app should not log the authentication tokens (just the status code), and instead hold them temporarily for accessing protected endpoints.
        - The CLI app should handle the access_token and refresh_token logic, should keep these safely in an object.

"As a loggged in user, I should be able to see my current balance.
I should also be able to deposit and withdraw from my balance." 
    Backend:
        - The api should have an endpoint /pokemart/balance where an app can GET the current balance of the logged in account.
        - The api should have an endpoint /pokemart/balance where an app can PUT an updated balance amount for the logged in account.
    Frontend:
        - The CLI app should be able to request from the backend the balance of the logged in user, and display it with pandas.
        - The CLI app should be able to ask the user if they want to deposit or withdraw, and how much to their current balance. 
        - The updated balance is then displayed, and the user is given the option to quit to the previous menu.

"As a logged in user, I should be able to see my account profile, which should contain
information like my first and last name, my age, and favorite Pokemon."
    Backend:
        - The api should have an endpoint /pokemart/profiles where an app can GET the profile of the logged in account.
        - The api should have an endpoint /pokemart/profiles where an app can PUT an updated profile for the logged in account.
    Frontend:
        - The CLI app should be able to request from the backend the profile of the logged in user, and display it with pandas.
        - The CLI app should allow a user to update their profile.
        - The updated profile is then displayed, and the user is given the option to quit to the previous menu.

"As a logged in user, I should be able to browse the store by category, and buy items from a cart.
I should be able see my previous orders.
I should be able to cancel a previous order and get a refund."
    Backend:
        - The api should have an endpoint /pokemart/store where an app can GET all of the items in the store. 
        - The api should have an endpoint /pokemart/store/<category> where an app can GET the items available from that category (e.g., Standard Pokeballs or Healing Items).
        - The api should have an endpoint /pokemart/categories where an app can GET all of the item categories.
        - The api should have an endpoint /pokemart/store/checkout where an app can POST an order by a logged in account.
            - The body of the request should have the item_id and qty, the created timestamp is automatically generated, and the total is calculated from the item cost.
        - The api should have an endpoint /pokemart/history where an app can GET all of the orders by a logged in account.
        - The api should have an endpoint /pokemart/history where an app can DELETE an order by a logged in account, and a refund can be issued at deletion.
    Frontend:
        - The CLI app should be able to display an option to browse all items, or a specific category. Items are displayed with pandas DataFrame formatting.
            - Categories are retrieved automatically and displayed as options.
        - The CLI app should have an option to add an item to the cart by id or name.
        - The CLI app should have an option to checkout, and place an order.
        - The CLI app should have an option to remove an item from the cart.
        - The CLI app should have an option to view all orders by the logged in user.
        - The CLI app should have an option to cancel an order by the logged in user.
        - The CLI app should display the balance.  

"As an admin, I should be able to see all users and whether or not they are admins. 
I should be able to delete a user.
I should be able see all users and their profiles.
I should be able to assign the admin role to a user or revoke it."
    Backend:
        - The api should have an endpoint /pokemart/users that is a protected endpoint, accessible only by admin users. 
            - An app can GET all accounts and their roles and profiles.
            - An app can DELETE an account and all of its data.
        - The api should have an endpoint /pokemart/user_role that is a protected endpoint, accessible only by admin users.
            - An app can POST a request with a body containing the account_id, and role_id to apply. 
            - An app can DELETE with the same composite key, and remove the admin role from a user.
    Frontend:
        - The CLI app should have an option to display all users and their respective data with pandas DataFrames. 
        - The CLI app should have the option to delete a user, or grant/revoke admin role.

"As an admin, I should be able to see all items in the store and their categories.
I should be able to add an item to the store.
I should be able to update an item in the store.
I should be able to delete an item in the store.
I should be able to see all orders from all users."
    Backend:
        - The api should have an endpoint /pokemart/store/inventory that is a protected endpoint, accessible only by admin users.
            - An app can GET all items and their information.
            - An app can POST a new item, and their information like name, cost, description, image, and category and create a new inventory item. 
                - MySQL will store name, cost, and category
                - MongoDB will store description, and image URL.
            - An app can PUT an existing item, and update their cost, description, image, or category.
            - An app can DELETE an existing item from the inventory. This should also delete from the mongodb collection.

        - The api should have an endpoint /pokemart/store/orders that is a protected endpoint, accessible only by admin users.
            - An app can GET all orders and their information from all accounts. 
    Frontend:
        - The CLI app should have the option to view the inventory and display them with a pandas DataFrame. 
        - The CLI app should have the option to filter by category and cost.
        - The CLI app should have the option to create/delete/update an item on the inventory.
        - The CLI app should have the option to view all the orders by all users. 