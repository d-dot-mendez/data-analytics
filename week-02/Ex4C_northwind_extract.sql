/*
4a) The name of the table that holds the items Northwind sells is
'products'. 
4b) The name of the table that holds the types/categories of the 
items Northwind sells is 'categories'. 

5a) The employee who has shares the name with a type of bird is
Peacock. 

6a) The query returned 77 records under the products table. 

7a) The category ID of seafood is the number 8. 
*/

USE northwind; 
SELECT * FROM products;
SELECT * FROM categories; 
SELECT
	OrderID,
    OrderDate,
    ShipName
    ShipCountry
FROM orders
LIMIT 50;