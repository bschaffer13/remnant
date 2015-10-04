--
-- File generated with SQLiteStudio v3.0.6 on Sat Oct 3 14:37:51 2015
--
-- Text encoding used: windows-1252
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: abilities
CREATE TABLE abilities (ability_id INTEGER PRIMARY KEY ON CONFLICT FAIL AUTOINCREMENT NOT NULL, name STRING (255) UNIQUE NOT NULL, description STRING, power INTEGER, class_name STRING, speed INTEGER, special_modifier DOUBLE);
INSERT INTO abilities (ability_id, name, description, power, class_name, speed, special_modifier) VALUES (1, 'Dragon Beam', 'Attack with high critical power', 0, NULL, NULL, 2);
INSERT INTO abilities (ability_id, name, description, power, class_name, speed, special_modifier) VALUES (2, 'Fire Breath', 'Unavoidable attack that hits all enemies', 20, NULL, NULL, NULL);
INSERT INTO abilities (ability_id, name, description, power, class_name, speed, special_modifier) VALUES (3, 'Dragon Breath', 'Increases crit chance against target', 0, 'DragonBreath', NULL, 2);

-- Table: remnant_fight_status
CREATE TABLE remnant_fight_status (remnant_instance_id INTEGER REFERENCES remnant_instances (remnant_instance_id) ON DELETE CASCADE NOT NULL, hp INTEGER NOT NULL, mana INTEGER NOT NULL, update_time INTEGER NOT NULL);

-- Table: remnant_instances
CREATE TABLE remnant_instances (remnant_instance_id INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT UNIQUE NOT NULL, remnant_id INTEGER REFERENCES sqlitestudio_temp_table (Remnant_ID) NOT NULL, level INTEGER NOT NULL, trait INTEGER NOT NULL, name STRING (255) NOT NULL, hp_modifier_lvl DOUBLE NOT NULL, speed_modifier_lvl DOUBLE NOT NULL, power_modifier_lvl DOUBLE NOT NULL, evasion DOUBLE NOT NULL, spirit INTEGER NOT NULL, critical_multiplier INTEGER NOT NULL, critical_chance DOUBLE NOT NULL, base_hp DOUBLE NOT NULL, speed DOUBLE NOT NULL, power DOUBLE NOT NULL);

-- Table: remnant_definitions
CREATE TABLE remnant_definitions (remnant_id INTEGER NOT NULL UNIQUE PRIMARY KEY ON CONFLICT ABORT AUTOINCREMENT, min_level INTEGER, name STRING (255) NOT NULL UNIQUE, class_name STRING (255), hp_base INTEGER NOT NULL, speed_base INTEGER NOT NULL, power_base INTEGER NOT NULL, evasion_base DOUBLE NOT NULL, spirit_base INTEGER NOT NULL, crit_mult_min INTEGER NOT NULL, crit_mult_max INTEGER NOT NULL, crit_chance DOUBLE NOT NULL, species STRING (255), Description STRING);
INSERT INTO remnant_definitions (remnant_id, min_level, name, class_name, hp_base, speed_base, power_base, evasion_base, spirit_base, crit_mult_min, crit_mult_max, crit_chance, species, Description) VALUES (1, 0, 'Fire Dragon', NULL, 90, 50, 10, 0.05, 10, 6, 8, 0.1, 'Dragon', NULL);

-- Table: remnant_abilities
CREATE TABLE remnant_abilities (ability_id INTEGER REFERENCES abilities (ability_id) NOT NULL, remnant_id INTEGER REFERENCES remnant_definitions (remnant_id) NOT NULL, level INTEGER NOT NULL);
INSERT INTO remnant_abilities (ability_id, remnant_id, level) VALUES (3, 1, 0);
INSERT INTO remnant_abilities (ability_id, remnant_id, level) VALUES (2, 1, 0);
INSERT INTO remnant_abilities (ability_id, remnant_id, level) VALUES (1, 1, 0);

-- Table: remnant_types
CREATE TABLE remnant_types (remnant_id INTEGER REFERENCES remnant_definitions (remnant_id), remnant_type INTEGER NOT NULL);
INSERT INTO remnant_types (remnant_id, remnant_type) VALUES (1, 1);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
