create DATABASE `webserver_users`;
use `webserver_users`;

DROP TABLE IF EXISTS `users`;

-- Table for usernames and passwords
CREATE TABLE `users`
    (
        `username` VARCHAR(25) NOT NULL PRIMARY KEY,
        `password`VARCHAR(100)
    );

-- Insert users into database
INSERT INTO `users` VALUES ("ryan", sha1("test"));