-- Query to order glam bands by lifespan
SELECT
	mb.band_name,
	COALESCE(mb.split, YEAR(now())) - mb.formed 
		AS `lifespan`
FROM metal_bands mb 
WHERE mb.`style` like '%Glam rock%';

