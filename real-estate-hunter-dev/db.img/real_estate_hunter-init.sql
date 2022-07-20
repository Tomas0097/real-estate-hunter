DROP DATABASE IF EXISTS real_estate_hunter;
CREATE DATABASE real_estate_hunter;

CREATE USER IF NOT EXISTS 'real_estate_hunter'@'%' IDENTIFIED BY '1122';
GRANT ALL PRIVILEGES ON real_estate_hunter.* TO 'real_estate_hunter'@'%';