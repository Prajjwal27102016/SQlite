
CREATE TABLE IF NOT EXISTS TOYS(
toy_id TEXT PRIMARY KEY,
toy_name TEXT,
category TEXT,
price REAL,
manufacturer TEXT
);

INSERT INTO TOYS (toy_id, toy_name, category, price, manufacturer) VALUES
('T001', 'Lego Brick Set', 'Construction', 29.99, 'Lego'),
('T002', 'Action Figure', 'Action', 15.99, 'Mattel'),
('T003', 'Lego Technic', 'Construction', 45.99, 'Lego'),
('T004', 'Board Game Adventure', 'Board Game', 34.99, 'Hasbro'),
('T005', 'Puzzle Brain Game', 'Puzzle', 12.99, 'Ravensburger'),
('T006', 'Lego Friends', 'Construction', 19.99, 'Lego'),
('T007', 'Action Hero Figure', 'Action', 22.50, 'DC Comics'),
('T008', 'Strategy Board Game', 'Board Game', 39.99, 'Hasbro'),
('T009', 'Logic Puzzle Game', 'Puzzle', 16.99, 'ThinkFun');


SELECT toy_id, toy_name, price 
FROM TOYS 
WHERE toy_name LIKE '%Lego%';

SELECT DISTINCT category 
FROM TOYS 
WHERE toy_name LIKE '%Brick%' OR toy_name LIKE 'B%';


SELECT * FROM TOYS;



