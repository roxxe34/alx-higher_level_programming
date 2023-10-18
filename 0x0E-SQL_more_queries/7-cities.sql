--  a script that creates the table cities  on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id),
    name VARCHAR(256)
);