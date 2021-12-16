-- Create user table with four columns
CREATE TABLE IF NOT EXISTS users (
	id int PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

