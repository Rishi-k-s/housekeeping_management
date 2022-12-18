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
SELECT * FROM userdetails

--@block
SHOW INDEX FROM userdetails

--@block
ALTER TABLE userdetails DROP INDEX password;

--@block
SELECT username,password FROM userdetails
WHERE username = 'u2'

--@block
SELECT username,name,password,user_role FROM userdetails WHERE username = 'u3'