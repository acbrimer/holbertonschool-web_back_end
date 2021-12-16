-- Create trigger on users table to reset valid email flag
DELIMITER $$
CREATE TRIGGER trig_reset_valid_email BEFORE UPDATE ON users
       FOR EACH ROW
       BEGIN
	       DECLARE current_email varchar(255)

	       SELECT u.email
	       INTO @current_email
	       FROM users AS u
	       WHERE u.id = NEW.id;
	       
	       IF current_email != NEW.email
	           SET NEW.valid_email = 0;
	       END IF;
       END;
$$
DELIMITER ;
