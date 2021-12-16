-- Procedure to compute avg score for users
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser 
	(
	IN user_id int
	)
	BEGIN
		
		-- join to aggregation sub-query to set avg
		UPDATE users AS u
		INNER JOIN (
			SELECT
				c.user_id
				, AVG(c.score) AS `average_score`
			FROM corrections AS c
			WHERE c.user_id = user_id
			GROUP BY c.user_id
		) AS a
			ON u.id = a.user_id
		SET u.average_score = a.average_score;
	END;
	$$
	
