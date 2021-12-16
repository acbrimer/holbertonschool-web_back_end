-- Creates a trigger on items table
DELIMITER $$
CREATE TRIGGER trig_decrease_items AFTER INSERT ON orders
       FOR EACH ROW
       BEGIN
           UPDATE items
          	SET quantity = quantity - 1
          	WHERE name = NEW.item_name;
       END;
$$
DELIMITER ;
