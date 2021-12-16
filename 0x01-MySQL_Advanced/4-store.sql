-- Creates a trigger on items table
CREATE TRIGGER trig_decrease_items AFTER INSERT ON items
FOR EACH ROW SET @quantity = @quantity - 1;

