-- lists number of records with the same score in table second_table of the database hbtn_0c_0 in my MySQL Server.
-- Sort list by number of records in descending order.
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
