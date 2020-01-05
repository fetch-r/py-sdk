create table `user` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `name` VARCHAR(512) NOT NULL,
  `user` BIGINT,
  `logUserId` BIGINT
);