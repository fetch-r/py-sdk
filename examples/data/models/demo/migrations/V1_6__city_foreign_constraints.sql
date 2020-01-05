ALTER TABLE `city` ADD FOREIGN KEY (`country`) REFERENCES `country`(`id`);
ALTER TABLE `city` ADD FOREIGN KEY (`timezone`) REFERENCES `timezone`(`id`);
