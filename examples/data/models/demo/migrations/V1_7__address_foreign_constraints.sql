ALTER TABLE `address`
  ADD FOREIGN KEY (`city`) REFERENCES `city`(`id`);
