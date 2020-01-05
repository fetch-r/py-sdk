ALTER TABLE `person`
  ADD FOREIGN KEY (`father`) REFERENCES `person`(`id`);

ALTER TABLE `person`
  ADD FOREIGN KEY (`mother`) REFERENCES `person`(`id`);
