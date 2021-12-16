-- Create index on first char of names.name
CREATE INDEX idx_name_first ON names (name(1));

