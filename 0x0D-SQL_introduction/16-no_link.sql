-- Lists all records of the table second_table. Don't list rows without a name value. Display the score and name
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
