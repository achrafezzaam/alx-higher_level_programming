-- Lists the number of records with the same score. Displays the score and number of records for that score
SELECT `score` ,COUNT(`score`) AS number FROM `second_table` GROUP BY `score`;
