USE Northwind;
SELECT DATABASE(); 

-- 1. What is the product name(s) of the most expensive products? 
SELECT ProductName
FROM products
WHERE  UnitPrice = (SELECT MAX(UnitPrice) FROM products);

--  What is the product name(s) and categories of the least expensive products? 
SELECT ProductName, CategoryName
FROM products
JOIN categories ON products.CategoryID = categories.CategoryID
WHERE  UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- 3. What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE shipvia = (SELECT ShipperID FROM shippers
				WHERE CompanyName = 'Federal Shipping'); 
                
-- What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID, ProductID
FROM `order details`
WHERE ProductID=
(SELECT ProductID
FROM products
WHERE ProductName =  'Sasquatch Ale');

-- 5. What is the name of the employee that sold order 10266? 
SELECT CONCAT(FirstName, ' ', LastName) AS Name
FROM employees e
JOIN orders o
ON e.EmployeeID = o.EmployeeID
WHERE o.OrderID =
(SELECT OrderID
FROM orders
WHERE OrderID = 10266);

-- 6. What is the name of the customer that bought order 10266?

SELECT ContactName
FROM customers c
JOIN orders o
ON c.CustomerID = o.CustomerID
WHERE o.ORDERID =
(SELECT OrderID 
FROM orders 
WHERE OrderID = 10266);
	
                


