-- Creates a view for students w/ score < 80 & no meeting within the last month
CREATE VIEW need_meeting
AS
	SELECT
		*
	FROM students AS s
	WHERE s.score < 80
	AND (
		ISNULL(s.last_meeting)
		OR s.last_meeting < DATE_ADD(CURDATE(),INTERVAL -1 MONTH)
		);
