import streamlit as st
import markdown

st.markdown('<h3 align="center">¿Quiénes somos?</h3>', unsafe_allow_html=True)

st.markdown(
"""
<p align='justify'>
En <b>G10 Consulting</b> desbloqueamos la sabiduría de sus datos de las organizaciones para que las decisiones se tomen de forma más inteligente y con mejores resultados. Somos una consultora de análisis de datos con sede Buenos Aires en tecnológica que empodera pequeños y medianos negocios, y compañías.
</p>""", unsafe_allow_html=True
)


# Define la lista de diccionarios de los developers
developers = [
    {
        'name': 'Gustavo Gonzales',
        'bio': 'Data Analyst & Machine Learning',
        'image': 'assets/gustavo.jpg'
    },
    {
        'name': 'Nicolas Callejas',
        'bio': 'Data Analyst',
        'image': 'assets/nicolas.jpg'
    },
    {
        'name': 'Roy Quillca',
        'bio': 'Data Engineer & Machine Learning',
        'image': 'assets/roy.jpg'
    },
    {
        'name': 'Lorenzo Prado',
        'bio': 'Data Engineer',
        'skills': 'ETL, Analisis Exploratorio',
        'image': 'assets/lorenzo.jpg'
    }
]

# Crea dos columnas para mostrar los perfiles de los developers
col1, col2 = st.columns(2)

# Itera a través de la lista de diccionarios y muestra la información de cada desarrollador
for i, developer in enumerate(developers):
    with eval(f"col{i % 2 + 1}"):
        st.markdown("---")
        st.markdown(f"**{developer['name'].upper()}**")
        # st.image(developer['image'], use_column_width=True)
        st.markdown(developer['bio'])
        st.markdown("---")


