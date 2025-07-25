CREATE DATABASE IF NOT EXISTS ppc_portal;
USE ppc_portal;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE ads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    pay_per_click DECIMAL(5,2) NOT NULL DEFAULT 0.10
);

CREATE TABLE clicks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    ad_id INT NOT NULL,
    ip_address VARCHAR(45),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (ad_id) REFERENCES ads(id)
);

INSERT INTO users (email, password) VALUES ('usuario@example.com', '123456');
INSERT INTO ads (title, url, pay_per_click) VALUES ('Anuncio 1', 'https://anuncio1.com', 0.10);
