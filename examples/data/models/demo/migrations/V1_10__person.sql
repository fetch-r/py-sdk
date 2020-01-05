create table `person` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `name` VARCHAR(512) NOT NULL,
  `father` BIGINT,
  `mother` BIGINT
);