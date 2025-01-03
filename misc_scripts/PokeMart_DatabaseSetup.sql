-- DROP DATABASE IF EXISTS PokeMart;
-- CREATE DATABASE PokeMart;
USE PokeMart;


DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Item_Categories;
DROP TABLE IF EXISTS Balances;
DROP TABLE IF EXISTS Accounts;

CREATE TABLE Accounts(
	account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_username VARCHAR(255) UNIQUE NOT NULL,
    account_password VARCHAR(255) NOT NULL,
    account_first_name VARCHAR(255),
    account_last_name VARCHAR(255)
);

CREATE TABLE Balances(
	balance_id INT PRIMARY KEY AUTO_INCREMENT,
    balance_owner INT,
    balance_amount INT,
    FOREIGN KEY (balance_owner) REFERENCES Accounts (account_id) ON DELETE CASCADE 
);

CREATE TABLE Item_Categories(
	cat_id INT PRIMARY KEY AUTO_INCREMENT,
    cat_name VARCHAR(255) NOT NULL
); 

CREATE TABLE Items(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
    item_cost INT NOT NULL,
    item_category INT NOT NULL,
    FOREIGN KEY (item_category) REFERENCES item_categories (cat_id) ON DELETE CASCADE
);

CREATE TABLE Orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_account_id INT NOT NULL,
    order_item_id INT,
    order_qty INT,
    FOREIGN KEY (order_item_id) REFERENCES Items (item_id) ON DELETE CASCADE
);

SELECT * FROM item_categories;
