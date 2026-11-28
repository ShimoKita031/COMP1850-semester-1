.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- YOU SHOULD RUN ANY 'UPDATES' AS SELECTS FIRST - it's very easy to accidentally update more than you intended..

--1
SELECT * FROM restaurants WHERE cuisine = 'italian' OR cuisine = 'ITALIAN';
UPDATE restaurants SET cuisine = 'Italian' WHERE cuisine = 'italian' OR cuisine = 'ITALIAN';

--2
SELECT * FROM restaurants;
UPDATE restaurants SET postcode = TRIM(UPPER(postcode));

--3
SELECT * FROM orders WHERE delivery_fee IS NULL;
UPDATE orders SET delivery_fee = '2.49' WHERE delivery_fee IS NULL;

--4
SELECT * FROM customers WHERE email LIKE '%@test.com';
DELETE FROM customers WHERE email LIKE '%@test.com';

--5
SELECT DISTINCT * FROM restaurants; --row with id being 99 found as duplicate
DELETE FROM restaurants WHERE restaurant_id = '99';