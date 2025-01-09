-- 1. Rodar script de criação e inserção de dados
-- https://gist.github.com/drsantos20/11ec2282f30a77166569924a75ae55de

-- 2. Extrair a quantidade de clientes cadastrados
SELECT COUNT(customer_id) FROM customer;

-- 3. Extrair os clientes que não fizeram compras
SELECT * FROM customer WHERE customer_id NOT IN (SELECT customer_id FROM customer_order);

-- 4. Extrair qual o produto mais vendido
SELECT product_id
FROM order_item
GROUP BY product_id
ORDER BY SUM(quantity) DESC
LIMIT 1;