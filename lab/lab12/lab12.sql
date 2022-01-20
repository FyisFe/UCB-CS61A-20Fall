.read data.sql 
CREATE TABLE bluedog AS
  SELECT color, pet 
  FROM students 
  WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest
  FROM students 
  WHERE smallest > 2 
  ORder BY smallest
  LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color
  FROM students as first, students as second 
  WHERE first.pet = second.pet AND first.song = second.song AND first.time < second.time;

CREATE TABLE sevens AS
  SELECT s.seven
  FROM students as s, numbers as n
  WHERE s.time = n.time AND s.number = 7 AND n."7" = "True";