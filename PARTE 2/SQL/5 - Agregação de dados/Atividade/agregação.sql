-- Tabela de produtos
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Tabela de estoque
CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product (id)
);

INSERT INTO product (name) VALUES 
('Notebook'),
('Smartphone'),
('Tablet'),
('Monitor');

INSERT INTO stock (product_id, quantity) VALUES 
(1, 10), -- Notebook
(1, 5),  -- Notebook
(2, 20), -- Smartphone
(3, 15), -- Tablet
(4, 8),  -- Monitor
(4, 12); -- Monitor

-- *EXERCÍCIO*
SELECT 
    product.name,
    SUM(stock.quantity)
FROM 
    product
INNER JOIN 
    stock
ON 
    product.id = stock.product_id
GROUP BY 
    product.name;

-- *RESULTADO*:
--     name    | sum
-- ------------+-----
--  Notebook   |  15
--  Smartphone |  20
--  Tablet     |  15
--  Monitor    |  20