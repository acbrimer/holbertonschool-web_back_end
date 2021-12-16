-- Creates a trigger on items table
DELIMITER $$
CREATE TRIGGER trig_decrease_items AFTER INSERT ON orders
       FOR EACH ROW
       BEGIN
           UPDATE items
          	SET quantity = quantity - NEW.number
          	WHERE name = NEW.item_name;
       END;
$$
DELIMITER ;
