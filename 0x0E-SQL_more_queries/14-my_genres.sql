-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT genres.name
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_g
ON genres.id = show_g.genre_id
INNER JOIN tv_shows AS shows
ON shows.id = show_g.show_id
WHERE shows.title = "Dexter"
ORDER BY genres.name;
