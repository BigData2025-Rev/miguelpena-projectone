-- DROP DATABASE IF EXISTS PokeMart;
-- CREATE DATABASE PokeMart;
USE PokeMart;

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Item_Categories;
DROP TABLE IF EXISTS Item_Category_Relational;
DROP TABLE IF EXISTS Balances;
DROP TABLE IF EXISTS Account_Details;
DROP TABLE IF EXISTS Account_Roles;
DROP TABLE IF EXISTS Accounts;


CREATE TABLE Account_Details(
	account_details_id INT PRIMARY KEY AUTO_INCREMENT,
    account_first_name VARCHAR(255),
    account_last_name VARCHAR(255),
    account_age INT
);

CREATE TABLE Accounts(
	account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_username VARCHAR(255) UNIQUE NOT NULL,
    account_password VARCHAR(255) NOT NULL,
    account_details_id INT NOT NULL,
    FOREIGN KEY (account_info_id) REFERENCES account_details (account_details_id) ON DELETE CASCADE
);

CREATE TABLE Balances(
	balance_id INT PRIMARY KEY AUTO_INCREMENT,
    balance_owner INT NOT NULL,
    balance_amount INT NOT NULL,
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

INSERT INTO roles(name, slug) VALUES ('Admin', 'admin');
SELECT * FROM roles;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE ROLES;
SET FOREIGN_KEY_CHECKS = 1;
SELECT * FROM roles;
DELETE FROM ROLES;

SELECT * FROM item_categories;
SELECT * FROM accounts;
TRUNCATE TABLE accounts;
SELECT * FROM account_details;
SELECT * FROM items;
SELECT * FROM item_category_relational;

DELETE FROM account_details;
DELETE FROM account_roles;
DELETE FROM balances;
DELETE FROM items;
DELETE FROM item_categories;
DELETE FROM item_category_relational;

ALTER TABLE items AUTO_INCREMENT = 1;
ALTER TABLE item_categories AUTO_INCREMENT = 1;