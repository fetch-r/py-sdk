create table `timezone` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` VARCHAR(512) NOT NULL,
  `time_offset` BIGINT NOT NULL
--   `instance_id` BIGINT NOT NULL,
--   `chain_id` BIGINT NOT NULL,
--   `log_user_id` BIGINT NOT NULL,
--   `log_date_added` DATETIME NOT NULL,
--   `log_is_log` BOOLEAN NOT NULL,
--   `log_previous_version_id` BIGINT
);