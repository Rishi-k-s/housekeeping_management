--@block
SHOW DATABASES;

--@block
DESCRIBE userdetails;

--@block
SHOW TABLES;
--@block
 SELECT username
 FROM userdetails
 WHERE username ='hotel1';


--@block
INSERT INTO userdetails
VALUES (UUID(),'u1','123','Sreejesh','SA');

--@block
CREATE TABLE userdetails(
    user_uid VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    name VARCHAR(255),
    user_role VARCHAR(255),
    sa_uid VARCHAR(255)
)
--@block
SELECT * FROM userdetails
--@block
SELECT dateAndTime,room,meal,hospitality,washroom,overall,remarks FROM reviews;

--@block
SELECT * FROM reviews;

--@block
SELECT * FROM hslocations;

--@block
SHOW INDEX FROM userdetails

--@block
ALTER TABLE userdetails DROP password;

--@block
SELECT username,password FROM userdetails
WHERE username = 'u2'

--@block
SELECT username,name,password,user_role FROM userdetails WHERE username = 'u3'

--@block
CREATE TABLE hslocations(
hsl_uid VARCHAR(255) PRIMARY KEY,
sa_uid VARCHAR(255) NOT NULL,
hk_uid VARCHAR(255),
place_name VARCHAR(255) UNIQUE);

--@block
ALTER TABLE userdetails
ADD sa_uid VARCHAR(255)

--@block
CREATE TABLE reviews(
    review_uid VARCHAR(255) PRIMARY KEY,
    hk_uid VARCHAR(255),
    sa_uid VARCHAR(255),
    dateAndTime DATETIME,
    room int,
    meal int,
    hospitality int,
    washroom int,
    overall int,
    remarks VARCHAR(255));

--@block
INSERT INTO reviews VALUES (
    UUID(),
    '92f92be3-7ece-11ed-b765-5811227fcdd6',
    '3580e648-7ecd-11ed-b765-5811227fcdd6',
    '2022-12-19 09:29:10',
    8,
    9,
    7,
    10,
    7,
    "Nice Place"
    )

--@block
ALTER TABLE reviews
ADD COLUMN room_uid VARCHAR(255)
AFTER sa_uid;

--@block
ALTER TABLE reviews
ADD COLUMN user_uid VARCHAR(255)
AFTER sa_uid;

--@block
UPDATE reviews
SET user_uid = '5706b3b6-7ecd-11ed-b765-5811227fcdd6';

--@block
ALTER TABLE reviews
CHANGE user_uid user_uid VARCHAR(255) AFTER room_uid;

--@block
SELECT AVG(room),AVG(meal),AVG(hospitality),AVG(washroom),AVG(overall) FROM reviews;

--@block
SELECT user_uid,username
FROM reviews NATURAL JOIN userdetails;

--@block
SELECT reviews.user_uid,userdetails.username,reviews.remarks
FROM reviews
INNER JOIN userdetails
ON reviews.user_uid=userdetails.user_uid
WHERE reviews.hk_uid ="92f92be3-7ece-11ed-b765-5811227fcdd6";


--@block
SELECT userdetails.name,hslocations.place_name
FROM userdetails
INNER JOIN hslocations
ON userdetails.user_uid =hslocations.hk_uid
WHERE userdetails.sa_uid = '7088951b-8aa2-11ed-ab30-5811227fcdd6';

--@block
SELECT userdetails.name,reviews.dateAndTime,reviews.room,reviews.meal,reviews.hospitality,reviews.washroom,reviews.overall,reviews.remarks 
FROM reviews 
INNER JOIN userdetails
ON reviews.user_uid = userdetails.user_uid
WHERE reviews.sa_uid = '{}';
--@block
DELETE FROM userdetails;

--@block
DELETE FROM reviews;


--@block
DELETE FROM hslocations;

--@block
SELECT place_name FROM hslocations WHERE hk_uid = '1062b0ca-8b8f-11ed-ab30-5811227fcdd6';