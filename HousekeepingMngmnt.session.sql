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