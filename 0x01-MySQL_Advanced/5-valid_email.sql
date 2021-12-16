-- Create trigger on users table to reset valid email flag
DELIMITER $$
CREATE TRIGGER trig_reset_valid_email BEFORE UPDATE ON users
       FOR EACH ROW
       BEGIN
	       IF OLD.email != NEW.email
	       THEN
	           SET NEW.valid_email = false;
	       END IF;
       END;
$$
DELIMITER 
