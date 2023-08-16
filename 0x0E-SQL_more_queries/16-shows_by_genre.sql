-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT shows.`title`, genres.`name`
FROM `tv_shows` AS shows
LEFT JOIN `tv_show_genres` AS show_g
ON shows.`id` = show_g.`show_id`
LEFT JOIN `tv_genres` AS genres
ON show_g.`genre_id` = genres.`id`
ORDER BY shows.`title`, genres.`name`;
