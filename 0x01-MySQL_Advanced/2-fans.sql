-- Query to get number of fans by country
SELECT
	mb.origin,
	SUM(mb.fans) AS 'nb_fans'
FROM metal_bands mb 
GROUP BY mb.origin 
ORDER BY SUM(mb.fans) DESC;

