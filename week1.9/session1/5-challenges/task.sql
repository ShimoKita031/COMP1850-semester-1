.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

--Bronze: 
SELECT * FROM drivers;
SELECT name, price FROM menu_items;
SELECT name FROM restaurants WHERE cuisine = 'Indian';

--Silver:
SELECT name, price, is_vegetarian FROM menu_items WHERE is_vegetarian = 1 AND price <= 8
ORDER BY price ASC;
SELECT * FROM orders WHERE status = 'cancelled'
ORDER BY order_time DESC LIMIT 10;

--Gold:
SELECT * FROM orders WHERE status = 'placed' AND order_time LIKE '2026-10%';
SELECT COUNT(*) FROM orders where strftime('%H:%M', order_time) >= '21:00';