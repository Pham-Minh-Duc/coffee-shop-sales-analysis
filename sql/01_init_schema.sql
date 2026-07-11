CREATE DATABASE IF NOT EXISTS CoffeeShopData;
USE CoffeeShopData;

CREATE TABLE IF NOT EXISTS raw_sales_data (
	transaction_id INT,
    transaction_date DATE,
    transaction_time TIME,
    transaction_qty INT,
    store_id INT,
    store_location VARCHAR(100),
    product_id INT,
    unit_price DECIMAL(10, 2),
    product_category VARCHAR(100),
    product_type VARCHAR(100),
    product_detail VARCHAR(255),
    PRIMARY KEY (transaction_id, store_id, product_id)
)