-- Creates a view for students w/ score < 80 & no meeting within the last month
CREATE VIEW need_meeting
AS
	SELECT
		*
	FROM students AS s
	WHERE s.score < 80
	AND (
		s.last_meeting IS NULL
		OR s.last_meeting > DATE_ADD(NOW(),INTERVAL -1 MONTH)
		);
