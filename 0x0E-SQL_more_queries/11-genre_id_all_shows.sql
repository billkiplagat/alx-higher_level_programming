-- LEFT JOIN keyword returns all records from the left table (tv_shows)
-- and the matching records from the right table (tv_show_genres)
-- The result is NULL if there is no match from the right table.
SELECT t.title, g.genre_id
FROM tv_shows AS t LEFT JOIN tv_show_genres AS g
ON t.id = g.show_id
ORDER BY t.title, g.genre_id;

