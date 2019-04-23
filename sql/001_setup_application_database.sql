CREATE DATABASE IF NOT EXISTS izanami CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'izanami'@'%' IDENTIFIED BY 'P@ssw0rd_izanami';
GRANT ALL PRIVILEGES ON izanami.* TO 'izanami'@'%';
