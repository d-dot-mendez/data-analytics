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
