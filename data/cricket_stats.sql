CREATE TABLE batting (
    Player VARCHAR(50),
    Innings INT,
    Runs INT,
    Balls INT,
    Outs INT,
    Avg FLOAT,
    SR FLOAT,
    HS INT,
    Fours INT,
    Sixes INT,
    Fifties INT,
    Hundreds INT
);

INSERT INTO batting VALUES
('Shubman Gill', 17, 890, 564, 15, 59.33, 157.8, 129, 85, 33, 4, 3),
('F du Plessis', 14, 730, 475, 13, 56.15, 153.68, 84, 60, 36, 8, 0),
('DP Conway', 15, 672, 481, 13, 51.69, 139.71, 92, 77, 18, 6, 0),
('V Kohli', 14, 639, 457, 12, 53.25, 139.82, 101, 65, 16, 6, 2),
('YBK Jaiswal', 14, 625, 382, 13, 48.08, 163.61, 124, 83, 26, 5, 1),
('SA Yadav', 16, 605, 334, 14, 43.21, 181.14, 103, 65, 28, 5, 1),
('RD Gaikwad', 15, 590, 400, 14, 42.14, 147.5, 92, 46, 30, 4, 0),
('DA Warner', 14, 516, 392, 14, 36.86, 131.63, 86, 69, 10, 6, 0),
('RK Singh', 14, 474, 317, 8, 59.25, 149.53, 67, 31, 29, 4, 0),
('Ishan Kishan', 15, 454, 318, 15, 30.27, 142.77, 75, 54, 18, 3, 0);

CREATE TABLE bowling (
    Player VARCHAR(50),
    Innings INT,
    Overs FLOAT,
    Runs INT,
    Wickets INT,
    Econ FLOAT,
    Avg FLOAT,
    SR FLOAT,
    FourWickets INT
);

INSERT INTO bowling VALUES
('Mohammed Shami', 17, 65, 522, 28, 8.03, 18.64, 13.93, 2),
('MM Sharma', 14, 44.1, 361, 27, 8.17, 13.37, 9.81, 2),
('Rashid Khan', 17, 67, 552, 27, 8.24, 20.44, 14.89, 1),
('PP Chawla', 16, 61, 495, 22, 8.11, 22.5, 16.64, 0),
('TU Deshpande', 16, 56.5, 564, 21, 9.92, 26.86, 16.24, 0),
('YS Chahal', 14, 52.5, 432, 21, 8.18, 20.57, 15.1, 3),
('CV Varun', 14, 52.4, 429, 20, 8.15, 21.45, 15.8, 1),
('RA Jadeja', 16, 57, 431, 20, 7.56, 21.55, 17.1, 0),
('M Pathirana', 12, 46.2, 371, 19, 8.01, 19.53, 14.63, 0),
('Mohammed Siraj', 14, 50, 375, 19, 7.5, 19.74, 15.79, 1);
