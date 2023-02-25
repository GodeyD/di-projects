-- 🌟 Exercise 1 : Items And Customers
-- CREATE TABLE items(
--  item_id SERIAL PRIMARY KEY,
--  item_name VARCHAR (50) NOT NULL,
--  item_price INT
-- );

-- CREATE TABLE customers(
--  customers_id SERIAL PRIMARY KEY,
--  fist_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (50) NOT NULL
-- );

-- INSERT INTO items
-- VALUES
-- (1,'Small Desk',100),
-- (2,'Large Desk',300),
-- (3,'Fan',80);

-- INSERT INTO customers
-- VALUES
-- (1,'Greg','Jones'),
-- (2,'Sandra','Jone'),
-- (3,'Scott','Scott'),
-- (4,'Trevor','Green'),
-- (5,'Melanie','Johnson');

-- select * from items
-- select * from items where item_price > 80 
-- select * from items where item_price <= 300
-- select * from customers where first_name = 'Smith'
-- select * from customers where last_name = 'Jones'
-- select * from customers where fist_name != 'Scott'