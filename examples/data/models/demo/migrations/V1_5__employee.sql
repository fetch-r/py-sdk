create table `employee` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `name` VARCHAR(512) NOT NULL,
  `email` VARCHAR(512),
  `age` BIGINT,
  `company` BIGINT
);