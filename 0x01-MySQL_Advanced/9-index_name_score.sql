-- Create an index on names.name (first char) and names.score
CREATE INDEX idx_name_first_score ON names (name(1), score);
