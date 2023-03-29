import pandas as pd
import numpy as np


import utils.paths as path

data_dir = path.make_dir_function('data')
raw_data_dir = data_dir('raw')
csv_files = raw_data_dir.glob('*.csv')



csv_files_dict = {}
for csv_file in csv_files:
    csv_files_dict[f"{csv_file.name.lower().split('.')[0]}"] = csv_file
    
    
def change_dt_format(df, list_cols):
    for col in list_cols:
        df[col] = pd.to_datetime(df[col])#.dt.strftime('%Y-%m-%d')
    return df

# Datasets usados para el modelo 1
df_admissions = pd.read_csv(csv_files_dict['admissions'])
df_patients = pd.read_csv(csv_files_dict['patients'])
df_icustays = pd.read_csv(csv_files_dict['icustays'])

# Cambiando el tipo de dato de las fechas
df_patients = change_dt_format(df_patients, ['dob', 'dod'])
df_icustays =  change_dt_format(df_icustays, ['intime', 'outtime'])
df_admissions = change_dt_format(df_admissions, ['admittime', 'dischtime'])

# Recálculo del LOS (lenght of stay)
df_icustays['los'] = (df_icustays['outtime'] - df_icustays['intime']).dt.total_seconds() / (3600*24)
# Calculo de duración de la hospitalización 
df_admissions['hospitalization_duration'] = (df_admissions['admittime'] - df_admissions['dischtime']).dt.total_seconds() / (3600*24)

# Selección de variables de los diferentes datasets
admissions_ml = df_admissions[["subject_id", "admission_type", "insurance", "language", "religion", "marital_status", "ethnicity", "hospital_expire_flag", "admission_location", "discharge_location", 'hospitalization_duration']]
patients_ml = df_patients[['subject_id', 'gender']]

# Selección de las variables del dataframe icustays
icustays_ml = df_icustays[['subject_id', 'los', 'first_careunit']]

# Dataframe original con variables seleccionadas para el modelado con ML
df = pd.merge(admissions_ml, patients_ml, on='subject_id', how='outer')
df = pd.merge(df, icustays_ml, on='subject_id', how='outer')


ethnicity_codes = {
    'BLACK/AFRICAN AMERICAN': 'BLACK AFRI_AMER',
    'UNKNOWN/NOT SPECIFIED': 'OTHER UNK_NS UNA_OBT',
    'WHITE': 'WHITE',
    'OTHER': 'OTHER UNK_NS UNA_OBT',
    'ASIAN': 'ASIAN',
    'HISPANIC OR LATINO': 'HISP LATIN',
    'HISPANIC/LATINO - PUERTO RICAN': 'PUERTO RICAN',
    'UNABLE TO OBTAIN': 'OTHER UNK_NS UNA_OBT',
    'AMERICAN INDIAN/ALASKA NATIVE FEDERALLY RECOGNIZED TRIBE': 'AMERERICAN INDIAN'
}

# Aplicamos la la transformacion de recategorización
df['ethnicity'] = df['ethnicity'].replace(ethnicity_codes)

# Reemplazo de valores completos de los idiomas
df['language'] = df['language'].str.replace('ENGL', 'ENGLISH')
df['language'] = df['language'].str.replace('SPAN', 'SPANISH')
df['language'] = df['language'].str.replace('RUSS', 'RUSSIAN')
df['language'] = df['language'].str.replace('POLI', 'POLISH')
df['language'] = df['language'].str.replace('MAND', 'MANDARIN')
# Reemplar los valores nulos por "Otro/OTHER"
df['language'] = df['language'].fillna('OTHER')

# Funcion para exportar el datframe a un archivo parquet
processed_data_dir = path.make_dir_function(['data','processed'])
def export_to_parquet(df, dir_path):
    df.to_parquet(dir_path)
# Exportación del dataframe
export_to_parquet(df, processed_data_dir('data_ml.parquet'))





    



