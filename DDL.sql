-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Banco
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Banco
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Banco` DEFAULT CHARACTER SET utf8 ;
USE `Banco` ;

-- -----------------------------------------------------
-- Table `Banco`.`Departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Departamento` (
  `dep_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad_poblacion` INT NOT NULL,
  PRIMARY KEY (`dep_id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Usuario` (
  `usr_id` INT NOT NULL,
  `nombre_alternativo` VARCHAR(50) NOT NULL,
  `clave` VARCHAR(4) NOT NULL,
  `nivel_usuario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`usr_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`AuditoriaES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`AuditoriaES` (
  `aud_id` INT NOT NULL,
  `fecha_entrada` DATETIME NOT NULL,
  `fecha_salida` DATETIME NOT NULL,
  `usr_id` INT NOT NULL,
  PRIMARY KEY (`aud_id`),
  INDEX `fk_auditoria_id_idx` (`usr_id` ASC) VISIBLE,
  CONSTRAINT `fk_auditoria_id`
    FOREIGN KEY (`usr_id`)
    REFERENCES `Banco`.`Usuario` (`usr_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Prioridad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Prioridad` (
  `prd_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`prd_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Municipio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Municipio` (
  `mun_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad_poblacion` INT NOT NULL,
  `dep_id` INT NOT NULL,
  `prd_id` INT NOT NULL,
  PRIMARY KEY (`mun_id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  INDEX `dep_id_idx` (`dep_id` ASC) VISIBLE,
  INDEX `fk_Municipio_Prioridad_idx` (`prd_id` ASC) VISIBLE,
  CONSTRAINT `dep_id`
    FOREIGN KEY (`dep_id`)
    REFERENCES `Banco`.`Departamento` (`dep_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Municipio_Prioridad`
    FOREIGN KEY (`prd_id`)
    REFERENCES `Banco`.`Prioridad` (`prd_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Cargo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Cargo` (
  `carg_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `salario` INT NOT NULL,
  PRIMARY KEY (`carg_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Empleado` (
  `emp_id` INT NOT NULL,
  `cedula` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`emp_id`),
  UNIQUE INDEX `cedula_UNIQUE` (`cedula` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Sucursal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Sucursal` (
  `suc_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `presupuesto_anual` INT NOT NULL,
  `mun_id` INT NOT NULL,
  PRIMARY KEY (`suc_id`),
  INDEX `mun_id_idx` (`mun_id` ASC) VISIBLE,
  CONSTRAINT `mun_id`
    FOREIGN KEY (`mun_id`)
    REFERENCES `Banco`.`Municipio` (`mun_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Contrato` (
  `contr_id` INT NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `fecha_fin` DATE NOT NULL,
  `emp_id` INT NOT NULL,
  `suc_id` INT NOT NULL,
  `carg_id` INT NOT NULL,
  PRIMARY KEY (`contr_id`),
  INDEX `fk_Contrato_Empleado1_idx` (`emp_id` ASC) VISIBLE,
  UNIQUE INDEX `emp_id_UNIQUE` (`emp_id` ASC) VISIBLE,
  INDEX `fk_Contrato_Sucursal_idx` (`suc_id` ASC) VISIBLE,
  INDEX `fk_Contrato_Cargo1_idx` (`carg_id` ASC) VISIBLE,
  CONSTRAINT `fk_emp_id`
    FOREIGN KEY (`emp_id`)
    REFERENCES `Banco`.`Empleado` (`emp_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Contrato_Sucursal`
    FOREIGN KEY (`suc_id`)
    REFERENCES `Banco`.`Sucursal` (`suc_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Contrato_Cargo`
    FOREIGN KEY (`carg_id`)
    REFERENCES `Banco`.`Cargo` (`carg_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Profesion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Profesion` (
  `prf_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`prf_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Detalle_Empleado_Profesion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Detalle_Empleado_Profesion` (
  `emp_id` INT NOT NULL,
  `prf_id` INT NOT NULL,
  INDEX `emp_id_idx` (`emp_id` ASC) VISIBLE,
  INDEX `prf_id_idx` (`prf_id` ASC) VISIBLE,
  CONSTRAINT `emp_id`
    FOREIGN KEY (`emp_id`)
    REFERENCES `Banco`.`Empleado` (`emp_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `prf_id`
    FOREIGN KEY (`prf_id`)
    REFERENCES `Banco`.`Profesion` (`prf_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco`.`Funcion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Banco`.`Funcion` (
  `func_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `carg_id` INT NOT NULL,
  PRIMARY KEY (`func_id`),
  INDEX `fk_Funcion_Cargo_idx` (`carg_id` ASC) VISIBLE,
  CONSTRAINT `fk_Funcion_Cargo`
    FOREIGN KEY (`carg_id`)
    REFERENCES `Banco`.`Cargo` (`carg_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
