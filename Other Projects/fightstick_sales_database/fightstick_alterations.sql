      --ALTERING TABLES IN FIGHTSTICK_DATABASE FOR CONSTRAINTS--
ALTER TABLE users
ADD PRIMARY KEY (user_id);

ALTER TABLE users
ADD CONSTRAINT FK_region_id FOREIGN KEY (region_id) REFERENCES regions(region_id) MATCH FULL;

ALTER TABLE products
ADD CONSTRAINT FK_category_id FOREIGN KEY (category_id) REFERENCES categories(category_id) MATCH FULL;

ALTER TABLE products
ADD CONSTRAINT FK_sale_id FOREIGN KEY (sale_id) REFERENCES sales(sale_id) MATCH FULL;

ALTER TABLE sales
ADD CONSTRAINT FK_product_name FOREIGN KEY (product_name) REFERENCES products(product_name) MATCH FULL;

ALTER TABLE sales
ADD CONSTRAINT FK_seller_id FOREIGN KEY (seller_id) REFERENCES users(user_id) MATCH FULL;

ALTER TABLE sales
ADD CONSTRAINT FK_channel_id FOREIGN KEY (channel_id) REFERENCES channels(channel_id) MATCH FULL;