-- # Criação da tabela Customers
CREATE TABLE Customers (
    id_customer SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    phone VARCHAR(15)
);

-- # Criação da tabela Products
CREATE TABLE Products (
    id_product SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    value FLOAT NOT NULL
);

-- # Criação da tabela Stock
CREATE TABLE Stock (
    id_product INTEGER,
    quantity FLOAT NOT NULL,
    FOREIGN KEY (id_product) REFERENCES Products(id_product)
);
