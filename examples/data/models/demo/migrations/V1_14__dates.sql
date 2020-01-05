create table `dates` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `timestamp` TIMESTAMP,
  `datetime` DATETIME,
  `date` DATE,
  `time` TIME
);