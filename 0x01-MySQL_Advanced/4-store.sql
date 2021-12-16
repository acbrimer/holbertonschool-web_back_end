-- Creates a trigger on items table
CREATE TRIGGER trig_decrease_items AFTER UPDATE ON orders
       FOR EACH ROW
       BEGIN
           UPDATE items
          	SET amount = amount - 1
          	WHERE name = NEW.item_name;
       END;
