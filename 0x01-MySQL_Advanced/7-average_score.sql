-- Creates proc to compute avg score for users
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser 
	(
	IN user_id int
	)
	BEGIN
		-- aggregate avg scores in CTE
		WITH avg_cte
		AS
		(
			SELECT
				c.user_id
				, AVG(c.score) AS `average_score`
			FROM corrections AS c
			WHERE c.user_id = user_id
			GROUP BY c.user_id
		)
		-- join to CTE to update users
		UPDATE users AS u
		INNER JOIN avg_cte AS a
			ON u.id = a.user_id
		SET u.average_score = a.average_score;
	END;
	$$
