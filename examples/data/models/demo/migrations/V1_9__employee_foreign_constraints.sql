ALTER TABLE `employee`
  ADD FOREIGN KEY (`company`) REFERENCES `company`(`id`);
