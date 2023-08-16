-- lists all cities contained in the database with state names
-- We create inner joins based on what the tables have in common
-- E.g sql is selecting all rows that have matching state_id
SELECT c.id, c.name, s.name
FROM cities AS c INNER JOIN states AS s
    ON c.state_id = s.id
ORDER BY c.id;
