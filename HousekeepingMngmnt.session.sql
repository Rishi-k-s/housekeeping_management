--@block
SHOW DATABASES;

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
SELECT * FROM userdetails