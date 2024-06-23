-- Create a second table with specific records
CREATE TABLE IF NOT EXISTS second_table
(id INT, name VARCHAR(256), score INT);
-- Query for Jhon
INSERT INTO second_table (id, name, score)
 VALUES (1, 'John', 10);
-- Query for Alex
INSERT INTO second_table (id, name, score)
 VALUES (2, 'Alex', 3);
-- Query for Bob
INSERT INTO second_table (id, name, score)
 VALUES (3, 'Bob', 14):
-- Query for George
INSERT INTO second_table (id, name, score)
 VALUES (4, 'George', 8);
