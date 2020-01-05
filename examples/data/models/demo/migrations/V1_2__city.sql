create table `city` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `name` VARCHAR(512) NOT NULL,
  `country` BIGINT NOT NULL,
  `timezone` BIGINT
--   `instance_id` BIGINT NOT NULL,
--   `chain_id` BIGINT NOT NULL,
--   `timezone_id` VARCHAR(512),
--   `log_user_id` BIGINT NOT NULL,
--   `log_date_added` DATETIME NOT NULL,
--   `log_is_log` BOOLEAN NOT NULL,
--   `log_previous_version_id` BIGINT
);