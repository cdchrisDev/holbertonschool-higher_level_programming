-- Create a second table with specific records
CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL,
	name VARCHAR(256),
	score INT
);
-- Insert data respectively
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
