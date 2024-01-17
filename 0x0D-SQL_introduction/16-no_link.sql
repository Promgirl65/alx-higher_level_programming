-- lists all records of table second_table of the database hbtn_0c_0 in my MySQL Server.
-- Does not list rows without a name value.
-- Lists records by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
