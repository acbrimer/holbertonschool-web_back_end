-- Create a stored proc to handle corrections
DELIMITER $$
CREATE PROCEDURE AddBonus 
	(
	IN user_id int, 
	IN project_name varchar(255),
	IN score float
	)
	BEGIN	
		
		-- insert new project if not exists
		IF NOT EXISTS (
			SELECT id FROM projects AS p
			WHERE p.name = @project_name
			)
			THEN
			INSERT INTO projects (name)
			VALUES (project_name);
		END IF;
		
		
		-- insert new correction
		INSERT INTO corrections (user_id, project_id, score)
		SELECT 
		@user_id,
		1,
		@score
		FROM projects AS p
			WHERE p.name = @project_name;
	
	END;
	$$
