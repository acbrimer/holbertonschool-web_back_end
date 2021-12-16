-- Creates a trigger on items table
CREATE TRIGGER trig_decrease_items BEFORE UPDATE ON items
       FOR EACH ROW
       BEGIN
           SET NEW.amount = NEW.amount - 1;
       END;
