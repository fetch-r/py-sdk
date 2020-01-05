create table `address` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `street` VARCHAR(512) NOT NULL,
  `city` BIGINT NOT NULL
--   `instance_id` BIGINT NOT NULL,
--   `chain_id` BIGINT NOT NULL,
--   `log_user_id` BIGINT NOT NULL,
--   `log_date_added` DATETIME NOT NULL,
--   `log_is_log` BOOLEAN NOT NULL,
--   `log_previous_version_id` BIGINT
);