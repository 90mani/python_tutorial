SELECT * FROM products WHERE product_expiry IN ('12', '24');
SELECT * FROM products WHERE product_expiry NOT IN ('36');
SELECT * FROM Products WHERE product_Price BETWEEN 100 AND 1000;
SELECT COUNT(product_id), product_name FROM products GROUP BY product_name;
SELECT * FROM products ORDER BY product_expiry;


