#stuid INT NOT null,
 #stuname VARCHAR(20),
 #mark1 INT ,
 #mark2 INT ,
 #mark3 INT ,
 #RANK INT 
 #);
 # SELECT *FROM school;
 # INSERT INTO school VALUES(101, "anu", 87, 90, 85,3);
 
#SELECT student.id, student.name, student.course, student.sem, student.attendance
#FROM student
#INNER JOIN school.stuid, school.stuname, school.mark1,school.mark2, school.mark3,school.RANK; 
  
#  SELECT course, sem, rank
#FROM student
#INNER JOIN school ON student.id = school.stuid;
SELECT student.name, school.stuname
FROM student
LEFT JOIN school ON student.id = school.stuid
ORDER BY student.name;
