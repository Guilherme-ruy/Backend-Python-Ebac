-- RECRIANDO AS TABELAS DE ESTOQUE E PRODUTOS COM RELACIONAMENTO

-- # Recriação da tabela Products
CREATE TABLE Products (
    id_product SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    value FLOAT NOT NULL
);

-- # Recriação da tabela Stock com relacionamento
CREATE TABLE Stock (
    id_stock SERIAL PRIMARY KEY,
    id_product INTEGER NOT NULL,
    quantity FLOAT NOT NULL,
    FOREIGN KEY (id_product) REFERENCES Products(id_product) ON DELETE CASCADE
);
