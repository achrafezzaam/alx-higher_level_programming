-- Lists all records with a score >= 10 in the table second_table. Display both the score and the name and ordered by score from greater to lower.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
