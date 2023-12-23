DROP TABLE IF EXISTS product;

CREATE TABLE product{
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    product_details TEXT NOT NULL,
    price REAL NOT NULL,
    ImageURL TEXT
};

INSERT INTO product (product_name, product_details, price, ImageURL,sex) VALUES
    ('Product 1', 'Details for Product 1', 19.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 2', 'Details for Product 2', 29.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 3', 'Details for Product 3', 39.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 4', 'Details for Product 4', 49.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 5', 'Details for Product 5', 59.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 6', 'Details for Product 6', 69.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 7', 'Details for Product 7', 79.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 8', 'Details for Product 8', 89.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 9', 'Details for Product 9', 99.99, '/Users/sezaigurle/Desktop/trendyol/database.db'),
    ('Product 10', 'Details for Product 10', 109.99, '/Users/sezaigurle/Desktop/trendyol/database.db');
