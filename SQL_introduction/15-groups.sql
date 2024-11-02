-- List num of records with same score in table
SELECT score,COUNT(*) AS 'number' FROM second_table
 GROUP BY score
 ORDER BY score DESC;
