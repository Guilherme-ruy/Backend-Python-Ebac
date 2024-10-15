-- Inserindo registros na tabela Customers
INSERT INTO Customers (full_name, email, cpf, phone) 
VALUES 
('Alice Pereira', 'alice.pereira@example.com', '12345678901', '11999998888'),
('Bruno Souza', 'bruno.souza@example.com', '23456789012', '11988887777'),
('Carla Dias', 'carla.dias@example.com', '34567890123', '11977776666');

-- Inserindo registros na tabela Products
INSERT INTO Products (name, value) 
VALUES 
('Blusa Básica Branca', 59.90), -- ID 1
('Blusa Estampada Feminina', 89.90), -- ID 2
('Blusa de Moletom Unissex', 119.90); -- ID 3

-- Inserindo registros na tabela Stock
INSERT INTO Stock (id_product, quantity) 
VALUES 
(1, 100), -- Estoque da Blusa Básica Branca
(2, 50),  -- Estoque da Blusa Estampada Feminina
(3, 30);  -- Estoque da Blusa de Moletom Unissex
