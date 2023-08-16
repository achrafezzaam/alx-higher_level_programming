-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.`name` AS `genre`, COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS genres
INNER JOIN `tv_show_genres` AS show_g
ON genres.`id` = show_g.`genre_id`
GROUP BY genres.`name`
ORDER BY `number_of_shows` DESC;
