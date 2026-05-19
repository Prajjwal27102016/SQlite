CREATE TABLE IF NOT EXISTS Batsman(
Batsman_NO TEXT PRIMARY KEY,
NAME TEXT,
RUNS TEXT
);
INSERT INTO Batsman VALUES
("5","James Hoog","15"),
("2","Nail Knite","13"),
("6","Pit Alex","11"),
("9","Mc Lyon","14"),
("7","Paul Adam","13"),
("3","Lauson Hen","12");

CREATE TABLE IF NOT EXISTS Baller(
Baller_NO TEXT,
Baller_name TEXT PRIMARY KEY,
WICKETS TEXT
);
INSERT INTO Baller VALUES
("1","nick rimando","1"),
("10","brad davis","2"),
("12","graham zusi","2"),
("14","julian green","3"),
("4","fabian johnson","3"),
("81","geoff cameron","1"),
("18","jozy altidor","2"),
("13","brad guzan","1");

SELECT * FROM BALLER;
SELECT * FROM Batsman;
SELECT Baller_name, WICKETS FROM Baller WHERE WICKETS > '1';



