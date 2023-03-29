import streamlit as st

# Define la lista de diccionarios de los developers
developers = [
    {
        'name': 'Roy Quillca',
        'bio': 'Soy un desarrollador con experiencia en Python y Django.',
        'skills': 'Python, Django',
        'image': 'https://example.com/developer1.jpg'
    },
    {
        'name': 'Gustavo Gonzales',
        'bio': 'Soy un desarrollador con experiencia en React y Node.js.',
        'skills': 'React, Node.js',
        'image': 'https://example.com/developer2.jpg'
    },
    {
        'name': 'Nicolas Callejas',
        'bio': 'Data Analyst',
        'skills': 'Data A',
        'image': 'https://example.com/developer3.jpg'
    },
    {
        'name': 'Lorenzo Prado',
        'bio': 'Data Engineer',
        'skills': 'ETL, Analisis Exploratorio',
        'image': 'https://example.com/developer4.jpg'
    }
]

# Crea dos columnas para mostrar los perfiles de los developers
col1, col2 = st.columns(2)

# Itera a través de la lista de diccionarios y muestra la información de cada desarrollador
for i, developer in enumerate(developers):
    with eval(f"col{i % 2 + 1}"):
        st.markdown(f"**{developer['name'].upper()}**")
        st.image(developer['image'], use_column_width=True)
        st.markdown(developer['bio'])
        st.markdown(f"**Skills:** {developer['skills']}")
        st.markdown("---")
