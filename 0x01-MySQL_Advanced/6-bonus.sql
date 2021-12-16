-- Creates proc to handle correction updates
DELIMITER $$
CREATE PROCEDURE AddBonus 
	(
	IN user_id int, 
	IN project_name varchar(255),
	IN score float
	)
	BEGIN	
		
		-- insert new project if not exists
		INSERT INTO projects (name)
			SELECT project_name
			WHERE NOT EXISTS (
				SELECT p.id FROM projects AS p
				WHERE p.name = project_name);
		
		
		-- insert correction
		INSERT INTO corrections (user_id, project_id, score)
		SELECT 
		user_id,
		p.id AS `project_id`,
		score
		FROM projects AS p 
		WHERE p.name = project_name;

	END;
	$$
