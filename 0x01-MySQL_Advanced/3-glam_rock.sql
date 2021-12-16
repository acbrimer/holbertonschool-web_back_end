-- Query to order glam bands by lifespan
SELECT
	mb.band_name,
	COALESCE(mb.split, 2021) - mb.formed 
		AS `lifespan`
FROM metal_bands mb 
WHERE mb.`style` like '%Glam rock%';

