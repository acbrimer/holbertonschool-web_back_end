-- Creates a function for safe division (0 when divide by 0)
DELIMITER $$
CREATE FUNCTION SafeDiv (a int, b int)
RETURNS float
DETERMINISTIC
BEGIN
	RETURN (SELECT
		CASE
			WHEN b = 0 THEN 0
		ELSE a / b
		END
		);
END;
$$
DELIMITER ;

