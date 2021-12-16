-- Create user table with three columns
CREATE TABLE IF NOT EXISTS users (
	id int PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
);

