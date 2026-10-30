/* 1. Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name 
	SELECT
		products.ProductID
        products.ProductName
        products.UnitPrice
        categories.CategoryName
	FROM products
    LEFT JOIN categrories
        ON products.CategoryID = categories.CategoryID
        
        */ 
USE northwind;
SELECT DATABASE(); 
SHOW TABLES;

-- Query for Question 1
SELECT ProductID, ProductName, UnitPrice, CategoryName
FROM products
LEFT JOIN categories 
ON products.CategoryID  = categories.CategoryID
ORDER BY CategoryName, ProductName;

/* 2. Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name */

SELECT ProductID, ProductName, UnitPrice, CompanyName
FROM products
LEFT JOIN suppliers
ON products.SupplierID = suppliers. SupplierID
WHERE UnitPrice > 75
ORDER BY ProductName;

/* 3. Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name */
SELECT ProductID, ProductName, UnitPrice, CategoryName, CompanyName
FROM products
JOIN categories ON products.CategoryID = categories.CategoryID
JOIN suppliers ON  suppliers.SupplierID = products.SupplierID
ORDER BY ProductName;

/*4. Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to */

SELECT OrderID, ShipName, ShipAddress, ShipName,CompanyName AS Shipper
FROM orders 
LEFT JOIN shippers
	ON orders.ShipVia = shippers.ShipperID 
WHERE ShipCountry = 'Germany'
order by Shipper, ShipName;

/* 5. Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name */

SELECT CompanyName AS Shipper,
	COUNT(OrderID) AS OrderCount
FROM orders 
LEFT JOIN shippers
	ON orders.ShipVia = shippers.ShipperID 
WHERE ShipCountry = 'Germany'
GROUP BY CompanyName
order by Shipper;

/* 6. Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale. */

SELECT orders.OrderID, orders.OrderDate, orders.ShipName, orders.ShipAddress
FROM orders
JOIN `order details` ON orders.OrderID =`order details`.OrderID
JOIN products ON products.ProductID = `order details`.ProductID
WHERE ProductName = 'Sasquatch Ale';







 
