-- Lists the number of records with the same score. Displays the score and number of records for that score
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
