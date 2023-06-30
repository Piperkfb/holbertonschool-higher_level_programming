-- creates a server user
CREATE USER 
    IF NOT EXISTS 'user_0d_1'@'localhost' 
    IDENTIFIED BY 'user_od_1.pwd';
GRANT ALL PRIVILEGES 
    ON *.*
    TO 'user_0d_1'@'localhost';
    IDENTIFIED BY 'user_0d_1pwd';
FLUSH PRIVILEGES;