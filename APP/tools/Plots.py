import pandas as pd
import numpy as np
from itertools import cycle

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler,MinMaxScaler, RobustScaler, normalize
from sklearn.cluster import KMeans


def plot_wscc(df, num_k_optimized):
    
    plt.style.use('seaborn')
    sns.set_style('whitegrid')
    
    # lista_y = cycle([5690.427, 5690.427, 11.68018*1000])
    lista_y = []
    color_cycle = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    x_max = 21

    scores = []

    for i in range(1,x_max):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(df)
        scores.append(kmeans.inertia_) # la inercia es la suma de los cuadrados de las distancias de las observaciones al centro del cluster más cercano
        if i == num_k_optimized:
            lista_y.append(kmeans.inertia_)

    fig = plt.Figure(figsize = (12, 5))
    fig = px.line(
                x=np.arange(1,x_max),
                y=np.array(scores),
                # color = next(color_list),
                # color_discrete_sequence = px.colors.qualitative.G10,
                height = 600,
                markers=True,
                labels={
                    'x': 'N° de Clusters',
                    'y': 'WCSS'
                }
                )
    color_font_line = next(color_cycle)
    fig.update_traces(line_color=color_font_line)
    # Configuración del diseño de elementos de la figura
    fig.update_layout(
        title={
            'text': f"Optimización del número de clusters en un análisis de clustering - {list(scalers.keys())[j].replace('_', ' ').title()}",
            # 'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font_size': 22,
            'font_color': color_font_line}
        )
    # Anotación
    fig.add_annotation(
            text="Número óptimo de clusters",
            x=num_k_optimized,
            y=lista_y,
            arrowhead=1,
            showarrow=True,
        )
    fig.show()


