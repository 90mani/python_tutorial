#SELECT * FROM student where id NOT IN (SELECT id FROM grade_mark)
#SELECT id FROM grade_mark;
#SELECT *FROM grade_mark;
#SELECT student.name,student.course,student.sem,grade_mark.grade
#FROM student,grade_mark
#WHERE student.id=grade_mark.id;
#SELECT student.name,student.course,student.course,student.attendance,grade_mark.name
#FROM student
#INNER JOIN grade_mark
#ON student.id=grade_mark.id;
# SELECT student.name,student.sem,student.attendance,grade_mark.persentag
 #FROM student
# LEFT JOIN grade_mark
# ON student.id=grade_mark.id;
SELECT student.name,student.sem,student.attendance,grade_mark.persentag,grade_mark.mark2
 FROM student
 right JOIN grade_mark
 ON student.id=grade_mark.id;
 #SELECT student.name,student.sem,student.attendance,grade_mark.persentag
 #FROM student
 #cross JOIN grade_mark
 #ON student.id=grade_mark.id;