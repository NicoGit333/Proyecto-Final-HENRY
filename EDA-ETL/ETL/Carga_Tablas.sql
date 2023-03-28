CREATE database FP_HENRY;
USE FP_HENRY;

-- PRIMERO CARGAMOS LAS TABLAS DE LA BASE DE DATOS
SET GLOBAL local_infile = true;
-- Cargamos las tablas de informacion de los pacientes: PATIENTS, ICUSTAYS y CALLOUT

DROP TABLE IF EXISTS patients;
CREATE TABLE patients(
	row_id INT NOT NULL,
	subject_id INT NOT NULL,
	gender VARCHAR(55),
	dob DATETIME DEFAULT NULL,
	dod DATETIME DEFAULT NULL,
	dod_hosp DATETIME DEFAULT NULL,
	dod_ssn DATETIME DEFAULT NULL,
	expire_flag INT DEFAULT 0);

LOAD DATA LOCAL INFILE 'C:/Users/PAVILION/OneDrive/Escritorio/PF_DATA07/Proyecto-Final-HENRY/EDA-ETL/RAW Datasets/PATIENTS.csv' 
INTO TABLE patients 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


DROP TABLE IF EXISTS icustays;
CREATE TABLE icustays(
	row_id INT NOT NULL,
	subject_id INT,
	hadm_id INT,
	icustay_id INT,
	dbsource VARCHAR(55),
	first_careunit VARCHAR(55),
	last_careunit VARCHAR(55),
	first_wardid INT,
	last_wardid INT,
	intime DATETIME,
	outtime DATETIME,
	los DECIMAL(10, 2));
    
LOAD DATA LOCAL INFILE 'C:/Users/PAVILION/OneDrive/Escritorio/PF_DATA07/Proyecto-Final-HENRY/EDA-ETL/RAW Datasets/ICUSTAYS.csv' 
INTO TABLE icustays
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


DROP TABLE IF EXISTS callout;
CREATE TABLE callout(
	row_id INT NOT NULL,
    subject_id INT,
    hadm_id INT,
    submit_wardid INT,
    submit_careunit VARCHAR(55),
    curr_wardid INT,
    curr_careunit VARCHAR(55),
    callout_wardid VARCHAR(55),
    callout_service VARCHAR(55),
    request_tele INT DEFAULT 0,
    request_resp INT DEFAULT 0,
    request_cdiff INT DEFAULT 0,
    request_mrsa INT DEFAULT 0,
    request_vre INT DEFAULT 0,
    callout_status VARCHAR (55),
    callout_outcome VARCHAR (55),
    discharge_wardid INT,
    acknowledge_status VARCHAR (55),
    createtime DATETIME,
    updatetime DATETIME,
    acknowledgetime DATETIME,
    outcometime DATETIME,
    firstreservationtime DATETIME,
    currentreservationtime DATETIME);
    
LOAD DATA LOCAL INFILE 'C:/Users/PAVILION/OneDrive/Escritorio/PF_DATA07/Proyecto-Final-HENRY/EDA-ETL/RAW Datasets/CALLOUT.csv' 
INTO TABLE callout
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


DROP TABLE IF EXISTS admissions;
CREATE TABLE admissions( 
	row_id INT NOT NULL,
    subject_id INT,
    hadm_id INT,
    admittime DATETIME,
    dischtime DATETIME,
    deathtime DATETIME,
    admission_type VARCHAR(55),
    admission_location VARCHAR(55),
    discharge_location VARCHAR(55),
    insurance VARCHAR(55),
    language VARCHAR(55),
    religion VARCHAR(55),
    marital_status VARCHAR(55),
    ethnicity VARCHAR(55),
    edregtime DATETIME,
    edouttime DATETIME,
    diagnosis VARCHAR(55),
    hospital_expire_flag INT DEFAULT 0,
    has_chartevents_data INT DEFAULT 0);
    
LOAD DATA LOCAL INFILE 'C:/Users/PAVILION/OneDrive/Escritorio/PF_DATA07/Proyecto-Final-HENRY/EDA-ETL/RAW Datasets/ADMISSIONS.csv' 
INTO TABLE admissions
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;



