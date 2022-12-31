SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Game`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Game` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Game` (
  `idGame` INTEGER NOT NULL AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  `saveRootPath` TEXT NOT NULL,
  `backupPath` TEXT NULL,
  PRIMARY KEY (`idGame`),
  UNIQUE INDEX `idGame_UNIQUE` (`idGame` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  UNIQUE INDEX `savePath_UNIQUE` (`saveRootPath` ASC) VISIBLE,
  UNIQUE INDEX `backupPath_UNIQUE` (`backupPath` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Backup`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Backup` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Backup` (
  `idSave` INTEGER NOT NULL AUTO_INCREMENT,
  `backupTime` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `fkIdGame` INTEGER NOT NULL,
  INDEX `fk_Backup_Game_idx` (`fkIdGame` ASC) VISIBLE,
  CONSTRAINT `fk_Backup_Game`
    FOREIGN KEY (`fkIdGame`)
    REFERENCES `mydb`.`Game` (`idGame`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
