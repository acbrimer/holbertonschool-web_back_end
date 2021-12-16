-- Query to order glam bands by lifespan
SELECT
	mb.band_name,
	COALESCE(mb.split, 2020) - mb.formed - 1
		AS `lifespan`
FROM metal_bands mb 
WHERE mb.`style` like '%Glam rock%';

