-- Lists all records of the table
-- except those without a name value
-- displays score and name (descending)
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
