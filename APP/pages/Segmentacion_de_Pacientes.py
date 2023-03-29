import streamlit as st

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler,MinMaxScaler, RobustScaler, normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity


import utils.paths as path

ml_data_dir = path.make_dir_function(['data', 'processed'])

# Creamos una copia del dataframe
df = pd.read_parquet(ml_data_dir('data_ml.parquet'))

# Creamos una copia del dataframe
df_ml = df.copy(deep=True)

# Función para agregar variables ficticias para reemplazar categóricas
def categorical_var_to_dummy(df, col_name):
    dummy = pd.get_dummies(df[col_name])
    df.drop(columns=col_name, axis=1, inplace=True)
    df = pd.concat([df, dummy], axis=1)
    return df

# Conversion  de las variables categóricas a variables dummy
df_ml = categorical_var_to_dummy(df_ml, 'admission_type')
df_ml = categorical_var_to_dummy(df_ml, 'insurance')
df_ml = categorical_var_to_dummy(df_ml, 'language')
df_ml = categorical_var_to_dummy(df_ml, 'religion')
df_ml = categorical_var_to_dummy(df_ml, 'marital_status')
df_ml = categorical_var_to_dummy(df_ml, 'ethnicity')
df_ml = categorical_var_to_dummy(df_ml, 'admission_location')
df_ml = categorical_var_to_dummy(df_ml, 'discharge_location')
df_ml = categorical_var_to_dummy(df_ml, 'first_careunit')
df_ml = categorical_var_to_dummy(df_ml, 'gender')

# Convertimos a minúsculas los nombres de las columnas del dataframe
df_ml.columns = [col.lower() for col in df_ml.columns]

# # No consideraremos la columna subject_id
df_ml = df_ml.iloc[::, 1:]



# ESCALAMIENTO DE DATOS

# Escalamos los datos con StanderScaler()
std_scaler = StandardScaler()
df_std_scaled = std_scaler.fit_transform(df_ml)

# Escalamos los datos con MinMaxScaler()
mm_scaler = MinMaxScaler()
df_mm_scaled = mm_scaler.fit_transform(df_ml)

# Escalamos los datos con RobustScaler()
robust_scaler = RobustScaler()
df_robust_scaled = robust_scaler.fit_transform(df_ml)


# Diccionario de los escalalers
scalers = {
    'standard_scaler': df_mm_scaled,
    'minmax_scaler': df_mm_scaled,
    'robust_scaler': df_robust_scaled,
    'sin_escalar': df_ml 
}


# Implementación del modelo K-Means
kmeans = KMeans(3)
kmeans.fit(df_ml)
# Etiquetas del clúster asociados a cada observación
labels = kmeans.labels_


# Dataframe de centroides de los dosclusters con datos escalados usando el método Standard Scaler
cc_std = pd.DataFrame(data=kmeans.cluster_centers_, columns=[df_ml.columns])
# Dataframe de centroides de los dosclusters con datos transformados al original del escalado con Standard Scaler
cc_sdt_inv_transf = pd.DataFrame(data=std_scaler.inverse_transform(cc_std), columns=[df_ml.columns])


y_kmeans = kmeans.fit_predict(df_std_scaled)

df_std_cluster = pd.concat([df, pd.DataFrame({'cluster':labels})], axis=1)

# print(df_std_cluster.shape)
# print(df_std_cluster.head(2))
# print(df_std_cluster['subject_id'].unique().shape)


def get_patient_by_sub_id(df, subject_id):
    mask_subject_id = df['subject_id'] == subject_id
    cluster = df[mask_subject_id]['cluster'][0]
    resp = {
        'subject_id': subject_id,
        'cluster': cluster
    }
    return resp

def get_patient_info(df, subject_id):
    mask_subject_id = df['subject_id'] == subject_id
    return df[mask_subject_id].iloc[0].to_dict()



subject_id = st.text_input('Inserte el id del paciente')
st.write('El id de paciente seleccionado es ', int(subject_id))


st.markdown(get_patient_by_sub_id(df_std_cluster, subject_id))
lista_subj_id = df_std_cluster['subject_id'].unique().values()

print(get_patient_by_sub_id(df_std_cluster, subject_id))
# print(get_patient_info(df_std_cluster, subject_id))
option = st.selectbox(
    'How would you like to be contacted?',
    tuple(lista_subj_id))

st.write('El paciente ha sido clasificado', get_patient_by_sub_id(df_std_cluster, option))

