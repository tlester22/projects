

--CREATING DATABASE WITH RELATED TABLES FROM CSV FILE 

			--creating users table--
CREATE TABLE users(
	user_id INTEGER,
    username VARCHAR(160),
    region_id INTEGER
);

INSERT INTO users(username, user_id, region_id)
SELECT distinct SELLER, SELLER_ID, REGION_ID FROM 'fightsticks_august2022.csv'
;

DELETE FROM users
WHERE username IN (SELECT username FROM
(SELECT username, count(*) FROM users
GROUP BY username
Having count(*) > 1)) AND user_id IS NULL;

DELETE FROM users
WHERE username IN (SELECT username FROM
(SELECT username, count(*) FROM users
GROUP BY username
Having count(*) > 1)) AND region_id IS NULL;

			--creating channel table--
CREATE TABLE channels(
	channel_id INTEGER PRIMARY KEY,
	channel_name VARCHAR(160)
);

INSERT INTO channels(channel_name, channel_id)
SELECT distinct CHANNEL, CHANNEL_ID FROM 'fightsticks_august2022.csv';




			--creating region table--
CREATE TABLE regions(
	region_id INTEGER PRIMARY KEY,
	region_abbrev VARCHAR(160)
);

INSERT INTO regions(region_abbrev, region_id)
SELECT distinct SELLER_REGION, REGION_ID FROM 'fightsticks_august2022.csv'
WHERE SELLER_REGION IS NOT NULL;




			--creating product table--
CREATE TABLE products (
	product_name VARCHAR(160) NOT NULL,
	sale_id INTEGER UNIQUE,
	price FLOAT,
	category_id INTEGER,
	PRIMARY KEY (product_name, sale_id)
);

INSERT INTO products(product_name, category_id, sale_id, price)
SELECT distinct PRODUCT_NAME, CATEGORY_ID, SALE_ID, PRICE FROM 'fightsticks_august2022.csv';



			--creating category table--
CREATE TABLE categories (
	category_id INTEGER PRIMARY KEY,
	category_name VARCHAR(160)
);

INSERT INTO categories(category_name, category_id)
SELECT DISTINCT CATEGORY, CATEGORY_ID FROM 'fightsticks_august2022.csv';

			--creating sales tables--
CREATE TABLE sales (
	sale_id INTEGER PRIMARY KEY,
	product_name VARCHAR(160),
	seller_id INTEGER,
	date_posted DATE,
	channel_id INTEGER
);

INSERT INTO sales(sale_id, product_name, seller_id, date_posted, channel_id)
SELECT SALE_ID, PRODUCT_NAME, SELLER_ID, DATE_POSTED, CHANNEL_ID FROM 'fightsticks_august2022.csv';

CREATE VIEW sales_analysis AS 
	SELECT s.sales_id, s.product_name, s.date_posted p.price, c.category_name, u.username, r.region_abbrev
	FROM sales As s
	LEFT JOIN products AS p 
	ON s.sale_id = p.sale_id AND s.product_name = p.product_name
	LEFT JOIN categories AS c 
	ON p.category_id = c.category_id
	LEFT JOIN users as u 
	ON c.seller_id = u.user_id
	LEFT JOIN regions as r 
	ON u.region_id = r.region_id;
	