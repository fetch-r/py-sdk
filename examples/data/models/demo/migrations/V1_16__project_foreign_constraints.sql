ALTER TABLE `project`
  ADD FOREIGN KEY (`company`) REFERENCES `company`(`id`);
