-- Creates a trigger on items table
CREATE TRIGGER trig_decrease_items AFTER INSERT ON items
FOR EACH ROW SET NEW.amount = NEW.amount - 1;

