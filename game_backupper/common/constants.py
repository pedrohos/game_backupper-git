# Common
BACKUP_FILEPATH_SUFFIX = "gamebkp"
BACKUP_FILEPATH_GLOB_PATTERN = "*.gamebkp"
BACKUP_VALID_FILENAME_REGEX_PATTERN = "[0-9]{8}-[0-9]{6}"

DB_ACTIVATE_FOREIGN_KEY = "PRAGMA foreign_keys = ON"

# Settings
SETTINGS_DEFAULT_BACKUP_PATH = "/Users/pedrohos/GameBackupper/Backups"

# Exceptions
# Settings
EXCEPTION_SETTINGS_EXCESSIVE_NUMBER_CONFIG_KEYS = "ERROR: Excessive number of configuration keys."
EXCEPTION_SETTINGS_INSUFFICIENT_NECESSARY_CONFIG_KEYS = "ERROR: Insufficient number of necessary configuration keys."
EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_PATH = "ERROR: Invalid path was set under the settings file."
EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_STRING = "ERROR: Invalid string was set under the settings file."
EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_FLOAT = "ERROR: Invalid float was set under the settings file."
EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_INT = "ERROR: Invalid int was set under the settings file."
EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_ATTRIBUTE = "ERROR: Invalid attribute was set under the settings file."
# Utils
EXCEPTION_UTILS_NONEXISTENT_PATH = "ERROR: Nonexistent backup path."
# LOGGER
# TODO: Check other places that may require logging
LOGGER_ERROR_SETTINGS_FAILED_TO_PARSE_JSON = "ERROR: Failed to parse configuration to json."
LOGGER_ERROR_SETTINGS_FAILED_TO_LOAD_SETTINGS = "ERROR: Failed to load user settings, loading default settings..."
LOGGER_WARNING_LOADING_DEFAULT_SETTINGS = "WARNING: Loading default settings."

# Database
DB_GENERATION_SQL_PATH = "./resources/db_generation.sql"

DB_FETCH_GAMES_SQL = "SELECT * FROM Game"
DB_GET_GAME_ID_SQL = "SELECT idGame FROM Game WHERE name = ?"
DB_ADD_GAME_SQL = "INSERT INTO Game(name, saveRootPath, backupPath) VALUES (?, ?, ?)"
DB_UPDATE_GAME_SQL = "UPDATE Game SET name = ?, saveRootPath = ?, backupPath = ? WHERE idGame = ?"
DB_DELETE_GAME_SQL = "DELETE from Game WHERE idGame = ?"

DB_FETCH_BACKUPS_SQL = "SELECT * FROM Backup WHERE fkIdGame = ?"
DB_ADD_BACKUP_SQL = "INSERT INTO Backup(fkIdGame) VALUES (?)"
DB_DELETE_BACKUP_SQL = "DELETE from Backup WHERE idSave = ?"

DB_CREATE_DATABASE_SQL = """
-- -----------------------------------------------------
-- Table `mydb`.`Game`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Game` ;

CREATE TABLE IF NOT EXISTS `Game` (
  `idGame` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `saveRootPath` TEXT NOT NULL,
  `backupPath` TEXT NULL);
CREATE UNIQUE INDEX `idGame_UNIQUE_idx` ON Game (`idGame`);
CREATE UNIQUE INDEX `name_UNIQUE_idx` ON Game (`name`);
CREATE UNIQUE INDEX `savePath_UNIQUE_idx` ON Game (`saveRootPath`);
CREATE UNIQUE INDEX `backupPath_UNIQUE_idx` ON Game (`backupPath`);


-- -----------------------------------------------------
-- Table `mydb`.`Backup`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Backup` ;

CREATE TABLE IF NOT EXISTS `Backup` (
  `idSave` INTEGER PRIMARY KEY AUTOINCREMENT,
  `backupTime` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `fkIdGame` INTEGER NOT NULL,
    FOREIGN KEY (`fkIdGame`)
    REFERENCES Game (`idGame`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
CREATE UNIQUE INDEX `fk_Backup_Game_idx` ON Backup (`fkIdGame`);
"""
