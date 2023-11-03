#SELECT * FROM student
#WHERE NAME IN ('renu','mani','revathi');
#SELECT * FROM student
#WHERE name not in ('renu', 'mani', 'revathi');
#SELECT * FROM student
#WHERE id IN (SELECT id FROM student);
SELECT * FROM student
WHERE id NOT IN (SELECT id FROM student);
