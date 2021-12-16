-- Creates a view for students w/ score < 80 & no meeting within the last month
CREATE VIEW need_meeting
AS
	SELECT
		*
	FROM students AS s
	WHERE s.score < 80
	AND (
		s.last_meeting IS NULL
		OR PERIOD_DIFF(
			EXTRACT(YEAR_MONTH FROM NOW()), 
			EXTRACT(YEAR_MONTH FROM s.last_meeting)) > 0
		);
