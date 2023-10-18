--  a script that creates the table states on your MySQL server.
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    name VARCHAR(256)
);