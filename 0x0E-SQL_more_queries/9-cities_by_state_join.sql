-- lists all cities contained in the database with state names
-- We create inner joins based on what the tables have in common
-- E.g sql is selecting all rows that have matching state_id
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities INNER JOIN hbtn_0d_usa.states
    ON cities.state_id = states.id
ORDER BY cities.id;
