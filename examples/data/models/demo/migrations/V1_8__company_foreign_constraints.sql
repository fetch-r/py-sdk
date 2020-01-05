ALTER TABLE `company`
  ADD FOREIGN KEY (`city`) REFERENCES `city`(`id`);
