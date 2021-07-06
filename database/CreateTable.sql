CREATE DATABASE IF NOT EXISTS database;
USE database;
CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL AUTO_INCREMENT,
  first_name VARCHAR (30) NOT NULL,
  last_name VARCHAR (30) NOT NULL,
  email VARCHAR (150) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (email)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
LOCK TABLES `users` WRITE;
INSERT INTO
  `
users`
VALUES
  (1, 'Yasser', 'Tahiri', 'test1@test.com'),
  (2, 'John', 'Doe', 'test2@test.com'),
  (3, 'Elliot', 'Alderson', 'test3@test.com');
UNLOCK TABLES;