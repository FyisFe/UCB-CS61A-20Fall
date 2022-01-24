
-- 2.1
SELECT Name FROM records WHERE Supervisor = "Oliver Warbucks";

-- 2.2
SELECT * FROM records WHERE Supervisor = name

-- 2.3
SELECT Name FROM records WHERE Salary > 50000 ORDER BY Name;

-- 3.1
SELECT m.Day, m.time 
FROM records as r, meetings as m
WHERE r.division = m.division AND r.Supervisor = "Oliver Warbucks";

-- 3.2
SELECT r1.name, r2.name FROM records as r1, records as r2, meetings as m1, meetings as m2
WHERE r1.division = m1.division AND r2.division = m2.division AND m1.time = m2.time AND m1.day = m2.day AND r1.name < r2.name;

-- 3.3
-- No, if a division has multiple meetings, then all pairs of individuals within the division will be returned multiple times.

-- 3.4
SELECT r1.name FROM records as r1, records as r2 
WHERE r1.Supervisor = r2.name AND r1.division != r2.division;

-- 4.1
SELECT Supervisor, sum(Salary) 
FROM records GROUP BY Supervisor;

-- 4.2
SELECT m.day 
FROM records AS r, meetings as m 
WHERE r.division = m.division
GROUP BY m.day
HAVING COUT(*) < 5;

-- 4.3
SELECT r1.division
FROM records as r1, records as r2
WHERE r1.name = r2.name AND r1.division = r2.division
GROUP BY r1.division
HAVING MAX(r1.Salary + r2.Salary) < 100000;

-- 5.1
CREATE TABLE num_taught AS
    SELECT professor AS professor, course AS course, count(*) AS time
    FROM course 
    GROUP BY professor, course;

-- 5.2
SELECT a.professor, b.professor, a.course 
FROM num_taught as a, num_taught as b
WHERE a.course = b.course AND a.professor < b.professor AND a.times = b.times;

-- 5.3
SELECT a.professor, b.professor
FROM course as a, course as b
WHERE a.professor < b.professor AND a.semester = b.semester AND a.course = b.course 
GROUP BY a.course, b.professor 
HAVING COUNT(*) > 1;