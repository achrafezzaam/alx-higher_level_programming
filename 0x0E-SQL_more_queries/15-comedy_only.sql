-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT shows.title
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS show_g
ON shows.id = show_g.show_id
INNER JOIN tv_genres AS genres
ON genres.id = show_g.genre_id
WHERE genres.name = "Comedy"
ORDER BY shows.title;
