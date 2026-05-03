CREATE TABLE supplier(
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier (SNO , SNAME , STATUS , CITY) VALUES
(27, 'Alan Stokes' , 22 , 'California'),
(36, 'Justin Mcarther' , 22 , 'LA'),
(90, 'Adem Mcarther', 22 , 'LA'),
(25, 'Dennis Foltyn' , 22 , 'California');

SELECT * FROM supplier