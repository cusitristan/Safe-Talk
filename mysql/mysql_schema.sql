CREATE DATABASE IF NOT EXISTS courses;

USE courses;

CREATE TABLE IF NOT EXISTS teachers(
    id INT(10) UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    addr VARCHAR(255) NOT NULL,
    phone INT NOT NULL
);