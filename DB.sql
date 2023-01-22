SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE=`TRADITIONAL`;

create database `game` default charset latin1;

USE `game` ;

-- -----------------------------------------------------
-- Table `PLAYER`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `game`.`Player` ;

CREATE  TABLE IF NOT EXISTS `game`.`Player` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(70) NOT NULL,
  `money` INT NOT NULL,
  `power` INT NOT NULL,
  `stamina` INT NOT NULL,
  `weapon` VARCHAR(70) NOT NULL,
  `shield` VARCHAR(70) NOT NULL,
  `style` VARCHAR(70) NOT NULL)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `WEAPON`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `game`.`Weapon` ;

CREATE  TABLE IF NOT EXISTS `game`.`Weapon` (
  `id` INT,
  `name` VARCHAR(70) primary KEY,
  `power` INT,
  `price` INT NOT NULL,
  `rand_coube` INT,
  `rand_coube_two` INT)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `SHIELD`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `game`.`Shield` ;

CREATE  TABLE IF NOT EXISTS `Shield`(
  `id` INT,
  `name` VARCHAR(70) PRIMARY KEY,
  `power` INT
  )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `shield`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `game`.`style` (
  `id` INT,
  `name` VARCHAR(70) PRIMARY KEY,
  `buf` FLOAT
)
ENGINE = InnoDB;


CREATE  TABLE IF NOT EXISTS `game`.`enemy`(
`name` VARCHAR(70) PRIMARY KEY,
`weapon` VARCHAR(70),
`power` INT
)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

SET AUTOCOMMIT=0;
USE `GAME`;
INSERT INTO PLAYER VALUES (1, "GLEB", 100, 10, 100, "KNIFE", "WOODS", "KARATE");
COMMIT;

SET AUTOCOMMIT=0;
USE `GAME`;
INSERT INTO WEAPON VALUES (1, "ROCK", 1, 0, 1, 5);
INSERT INTO WEAPON VALUES (2, "KNIFE", 5, 50, 1, 5);
INSERT INTO WEAPON VALUES (3, "BOW", 10, 100, 1, 10);
COMMIT;

SET AUTOCOMMIT=0;
USE `GAME`;
INSERT INTO SHIELD VALUES (1, "WOODS", 10);
INSERT INTO SHIELD VALUES (2, "METAL", 100);
INSERT INTO SHIELD VALUES (3, "DIAMOND", 200);
COMMIT;

SET AUTOCOMMIT=0;
USE `GAME`;
INSERT INTO STYLE VALUES (1, "BOX", 0.2);
INSERT INTO STYLE VALUES (2, "KARATE", 0.5);
COMMIT;



ALTER TABLE PLAYER
ADD FOREIGN KEY (WEAPON) REFERENCES WEAPON(NAME);
  
ALTER TABLE PLAYER
ADD FOREIGN KEY (SHIELD) REFERENCES SHIELD(NAME);

ALTER TABLE PLAYER
ADD FOREIGN KEY (STYLE) REFERENCES STYLE(NAME);